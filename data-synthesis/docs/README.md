# Data Synthesis

![synthesized](/docs/Images/synthesized.jpg)

Sample expected output

## Description
This project directory embeds the generated images into DIV2k dataset from the MirFlickr25k dataset after performing random transformations.

This is the final step before the dataset is ready to be used for training on the selected benchmark models:

- [BiSeNet](https://github.com/GeorgeSeif/Semantic-Segmentation-Suite/tree/master/models)
- [MobileUNet](https://github.com/GeorgeSeif/Semantic-Segmentation-Suite/tree/master/models)
- [UNet](https://github.com/alain-cheng/Semantic-Segmentation-Suite/tree/master/models)
- [MobileBiSeNet (Ours)](https://github.com/alain-cheng/Semantic-Segmentation-Suite/tree/master/models)

After running the full project, you should see the dataset in this directory: `./assets/synthesized`. 

*Note: the dataset is not in the correct folder structure, please follow the appropriate structure based on the documentation found below. We used the linux `mv` command to fix this manually.*

[link](https://github.com/alain-cheng/Semantic-Segmentation-Suite/tree/master)

        https://github.com/alain-cheng/Semantic-Segmentation-Suite/tree/master

### How to use
1. Run `python main.py`

## Datasets Used

This process uses two different datasets:

- [DIV2K](http://data.vision.ee.ethz.ch/cvl/DIV2K/DIV2K_train_HR.zip)

        http://data.vision.ee.ethz.ch/cvl/DIV2K/DIV2K_train_HR.zip

- MirFlickr25k (Preprocessed)

        Must perform Step #1 and #2 of this project to obtain.