# Celtic Pipeline: Proto-Celtic Reconstruction

This directory contains the Celtic comparative linguistics pipeline for proto-language reconstruction, ported from [anTadhg/caprWIP-Celtic](https://github.com/anTadhg/caprWIP-Celtic).

## Overview

The Celtic pipeline models sound changes from Proto-Celtic to its daughter languages using finite-state transducers (FSTs) built with Foma.

**Daughter languages covered:**
- Old Irish, Middle Irish
- Old Welsh, Middle Welsh
- Old Breton, Middle Breton
- Old Cornish, Middle Cornish
- Gaulish, Celtiberian

## Directory Structure

```
Celtic/
├── data/
│   └── celtic-aligned-final.tsv     # Aligned cognate wordlist (proto-forms + daughter reflexes)
└── fsts/
    ├── celtic.txt                    # Main Proto-Celtic → daughter language FST
    ├── celtic.txt.bak                # Backup of FST
    ├── celtic_1.txt                  # Earlier iteration of the Celtic FST
    ├── mw_test.foma                  # Middle Welsh foma test script
    ├── mw_trace.foma                 # Middle Welsh foma trace script
    ├── old_irish.bin                 # Compiled FSTs per daughter language
    ├── middle_irish.bin
    ├── old_welsh.bin
    ├── middle_welsh.bin
    ├── old_breton.bin
    ├── middle_breton.bin
    ├── old_cornish.bin
    ├── middle_cornish.bin
    ├── gaulish.bin
    └── celtiberian.bin
```

## Usage

### Load in CAPR UI

To use Celtic data in the web interface, edit `docker-compose.yml` to mount Celtic paths:

```yaml
volumes:
  - ./server:/usr/app
  - ./Celtic/data:/usr/app/data
  - ./Celtic/fsts:/usr/app/fsts
```

Then restart Docker and select `celtic-aligned-final.tsv` in the UI dropdown.

### Compile the FST

```bash
docker compose exec -T backend bash -c "cd /usr/app && foma -q -l fsts/celtic.txt -e quit"
```
