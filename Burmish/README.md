# Burmish Pipeline: Proto-Burmish Reconstruction

This directory contains the Burmish comparative linguistics pipeline for proto-language reconstruction.

## Overview

The Burmish pipeline uses LingPy/LingRex for:
- Automatic cognate detection
- Sound correspondence identification
- Proto-form reconstruction

## Directory Structure

```
Burmish/
├── data/
│   └── burmish-aligned-final.tsv     # Main aligned wordlist
├── fsts/
│   └── burmish.txt                   # Burmish FST rules
├── pipeline/
│   ├── burmish-data.tsv              # Input data
│   ├── lexicon-pipeline.py           # Processing scripts
│   └── output/                       # Pipeline stage outputs
├── orthoprofiles/
│   └── profile-*.tsv                 # Orthographic profiles per doculect
└── reconstruct/
    └── *.bin                         # Reconstruction FSTs per doculect
```

## Usage

### Load in CAPR UI

To use Burmish data in the web interface, edit `docker-compose.yml` to mount Burmish paths:

```yaml
volumes:
  - ./server:/usr/app
  - ./Burmish/data:/usr/app/data
  - ./Burmish/fsts:/usr/app/fsts
```

Then restart Docker and select `burmish-aligned-final.tsv` in the UI.

### Run pipeline

```bash
cd Burmish/pipeline
python lexicon-pipeline.py
```

## Citation

Xun Gong & Nathan Hill (2020). *Materials for an Etymological Dictionary of Burmish*. Zenodo. https://doi.org/10.5281/zenodo.4311182
