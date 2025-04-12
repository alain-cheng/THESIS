# TOWARDS AN IMPROVEMENT OF STEGASTAMP’S SPEED IN DETECTING HIDDEN MESSAGES IN IMAGES

![pipeline](/docs/Images/synthesis-pipeline.png)

The synthesized dataset pipeline described in this doc.

## Notice !

Image annotations produced after completion of `./data-synthesis/main.py` are dirty and are cleaned through a different repository: https://github.com/alain-cheng/Semantic-Segmentation-Suite.git through `utils/data_cleaning.py`


## Description

Repository for THS-ST handling the synthesized dataset pipeline.

Link to the [StegaStamp](https://arxiv.org/abs/1904.05343) paper

## Usage

This repository contains multiple directories that must be executed in the following steps:

1. `./mirflickr25k-preprocessing`

    - get the mirflickr dataset from [here](https://press.liacs.nl/mirflickr/mirdownload.html)
    - unzip the mirflickr then run `split.py` before running `main.py`

2. `./image-perturbation`

    - run `main.py`

3. `./data-synthesis`

    - run `main.py`

### Steps Info

#1 - Generates StegaStamp encodings onto a series of images from the MIRFLICKR25K Dataset.

#2 Applies perturbation to all images from step #1 such as Perspective Warp.

#3 Embeds the image data from step #2 onto images from the DIV2K High Resolution Dataset.

After following the steps, we use this [repository](https://github.com/alain-cheng/Semantic-Segmentation-Suite/tree/master) for training the models:

    https://github.com/alain-cheng/Semantic-Segmentation-Suite/tree/master

## Dev Notes

### Export Requirements

```sh
pip freeze > requirements.txt
```