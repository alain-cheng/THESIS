# Improving StegaStamp's Detection of Hidden Messages in Images

## Description

Repository for THS-ST.

[StegaStamp](https://arxiv.org/abs/1904.05343)

## Usage

This repository contains multiple different related projects that must be executed in the following sequence:

1. `./mirflickr25k-preprocessing`
2. `./image-augmentation`
3. `./data-synthesis`

### Quick Info

- `./mirflickr25k-preprocessing` Generates StegaStamp encodings onto a series of images from the MIRFLICKR25K Dataset while generating the necessary labels for semantic segmentation. The outputs are images and labels of 400x400 px. Labels are always saved as PNG while image data are saved on JPG. Its output directory is at `assets/stegastamp-encoded`.
- `./image-augmentation` Performs image augmentation techniques on a select amount of images from the previous step such as Perspective Warp, Blur, Color Shift, etc. Output data will remain at 400x400 px.
- `./data-synthesis` Embeds the 400x400 px image data from the previous step onto images from the DIV2K High Resolution Dataset. The output is a synthesized data with an output resolution of 800x800 px. 

## Dev Notes

### Export Requirements

```sh
pip freeze > requirements.txt
```