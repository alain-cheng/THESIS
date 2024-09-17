# Performing Image Augmentation

## Description
This project directory transforms the encoded images from the MIRFLICKR Dataset via the following different augmentation methods:
- Perspective Warp
- Motion Blur
- Color Shift
- Gaussian Noise
- JPEG Compression

Each method is implemented with an internal random variable to ensure variation.

![perturbed](/docs/Images/perturbed.jpg)

A sample image of the expected output is shown.

After running, processed images are saved in `./assets/perturbed`.

## Setup

### Dataset

This project dir assumes that `../mirflickr25k-preprocessing` has been executed.

