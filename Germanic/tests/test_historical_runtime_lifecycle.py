"""Disposable historical runtimes must clean up on every owned failure path."""
import subprocess
from unittest.mock import patch

import pytest

from historical_sc035 import historical_runtime


@pytest.mark.parametrize("failure", [None, "start", "source", "build", "body"])
def test_historical_container_is_removed_without_writable_host_mounts(failure):
    calls = []

    def output(command, **kwargs):
        calls.append(command)
        if command[:3] == ["docker", "compose", "images"]:
            return "image-id\n"
        if command[:2] == ["git", "show"]:
            return b"define Historical [a -> b];"
        assert command[:2] == ["docker", "create"]
        mounts = [command[i + 1] for i, argument in enumerate(command) if argument == "--volume"]
        assert mounts and all(mount.endswith(":ro") for mount in mounts)
        assert all(":/usr/app:" not in mount for mount in mounts)
        return "owned-container-id\n"

    def run(command, **kwargs):
        calls.append(command)
        point = ("start" if command[1] == "start" else
                 "source" if command[1:3] == ["exec", "-i"] else
                 "build" if command[1] == "exec" else None)
        if point == failure and failure is not None:
            raise subprocess.CalledProcessError(1, command)
        return subprocess.CompletedProcess(command, 0, "", "")

    with patch("historical_sc035.subprocess.check_output", side_effect=output), \
            patch("historical_sc035.subprocess.run", side_effect=run):
        if failure:
            with pytest.raises((subprocess.CalledProcessError, RuntimeError)):
                with historical_runtime("historical-commit"):
                    if failure == "body":
                        raise RuntimeError("assay failed")
        else:
            with historical_runtime("historical-commit") as execute:
                assert callable(execute)
    assert calls[-1] == ["docker", "rm", "--force", "owned-container-id"]
