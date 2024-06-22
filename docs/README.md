# Improving StegaStamp's Detection of Hidden Messages in Images

## Notice !

Image annotations produced from `./data-synthesis/main.py` for training benchmark models are dirty and are currently cleaned through a different repository: 

**BiSeNet & MobileUNet**

https://github.com/alain-cheng/Semantic-Segmentation-Suite.git through `utils/data_cleaning.py`, `utils/extension_cleaning.py`, & `utils/filename_cleaning.py`

**BiSeNet V2**

No cleaning performed. Uses `./data-synthesis/main-v2.py`.

## Description

Repository for THS-ST.

Link to the [StegaStamp](https://arxiv.org/abs/1904.05343) paper

## Usage

This repository contains multiple different related projects that must be executed in the following sequence:

1. `./mirflickr25k-preprocessing`
2. `./image-perturbation`
3. `./data-synthesis`

### Quick Info

- `./mirflickr25k-preprocessing` Generates StegaStamp encodings onto a series of images from the MIRFLICKR25K Dataset while generating the necessary labels for semantic segmentation. The outputs are images and labels of 400x400 px. Labels are always saved as PNG while image data are saved on JPG. Its output directory is at `assets/stegastamp-encoded`.
- `./image-perturbation` Performs image perturbation on images from the previous step such as Perspective Warp, Blur, Color Shift, etc.
- `./data-synthesis` Embeds the image data from the previous step onto images from the DIV2K High Resolution Dataset.



## Dev Notes

### Export Requirements

```sh
pip freeze > requirements.txt
```