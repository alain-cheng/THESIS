# Improving StegaStamp's Detection of Hidden Messages in Images

![pipeline](/docs/Images/synthesis_pipeline.jpg)

The synthesized dataset pipeline described in this doc.

## Notice !

Image annotations produced after completion of `./data-synthesis/main.py` are dirty and are cleaned through a different repository: https://github.com/alain-cheng/Semantic-Segmentation-Suite.git through `utils/data_cleaning.py`


## Description

Repository for THS-ST handling the synthesized dataset pipeline.

Link to the [StegaStamp](https://arxiv.org/abs/1904.05343) paper

## Usage

This repository contains multiple directories that must be executed in the following steps:

1. `./mirflickr25k-preprocessing`
2. `./image-perturbation`
3. `./data-synthesis`

### Steps Info

#1 - Generates StegaStamp encodings onto a series of images from the MIRFLICKR25K Dataset while generating the annotations for semantic segmentation task. The outputs are of dimensions 400x400 px. All outputs can be found on `./assets`.

#2 Applies perturbation to all images from step #1 such as Perspective Warp, Blur, Color Shift, etc. This creates a new directory found on `./assets`.

#3 Embeds the image data from step #2 onto images from the DIV2K High Resolution Dataset.

After following the steps, please go to this [repository](https://github.com/alain-cheng/Semantic-Segmentation-Suite/tree/master) for training the models:

    https://github.com/alain-cheng/Semantic-Segmentation-Suite/tree/master

## Dev Notes

### Export Requirements

```sh
pip freeze > requirements.txt
```