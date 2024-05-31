# MirFlickr25k Dataset Encoding

## Notice

### Important!
The project has been run strictly using **Python 3.7.16** & **Tensorflow 1.13.1**. Using other versions than what is stated may cause the project to not run as intended.

## Description

This project directory encodes and/or resizes images from the MirFlickr dataset via StegaStamp encoding in preparation for image augmentation through the `../image-augmentation` project directory.

### Examples

<img src="../Images/encoded.png" alt=alt-text-01 width=1000>

## Dataset

The MirFlickr dataset used in this project can be obtained from the following download [link](http://press.liacs.nl/mirflickr/mirflickr25k.v3b/mirflickr25k.zip):

    http://press.liacs.nl/mirflickr/mirflickr25k.v3b/mirflickr25k.zip

## StegaStamp Encoder Model

The StegaStamp encoder model used in this project can be downloaded from [here](https://drive.google.com/drive/folders/1EHvFEVXufdiaHM15wSAXcxFFzIgaMRFn?usp=drive_link).

Once the model has been downloaded, make sure the model is in the same directory of this project and the model file is structured as follows:

    ├── saved_models
        ├── saved_model.pb          
        ├── variables
            ├── variables.data
            ├── variables.index

## Installation

The dependencies used in this project can be installed by running:

```sh
pip install -r requirements.txt
```

- Tensorflow is not included in the requirements.txt