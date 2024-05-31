# MirFlickr25k Dataset Encoding

## Description

This project has been run strictly using **Python 3.7.16** & **Tensorflow 1.13.1**. Using other versions than what is stated may cause the project to not run as intended.

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