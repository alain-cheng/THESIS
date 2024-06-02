# Data Synthesis

## Description
This project directory embeds the generated images into DIV2k dataset from the MirFlickr25k dataset after performing random transformations.

This is the final step before the dataset is ready to train on the selected benchmark models:

- [BiSeNet V1](https://github.com/GeorgeSeif/Semantic-Segmentation-Suite/tree/master/models)
- [BiSeNet V2](https://arxiv.org/abs/2004.02147)
- [HRNet](https://paperswithcode.com/method/hrnet#:~:text=HRNet%2C%20or%20High-Resolution%20Net,representations%20through%20the%20whole%20process.)


## Datasets Used

This project uses two different datasets that can be downloaded from the following links:

- [DIV2K](http://data.vision.ee.ethz.ch/cvl/DIV2K/DIV2K_train_HR.zip)

        http://data.vision.ee.ethz.ch/cvl/DIV2K/DIV2K_train_HR.zip

- [MirFlickr25k (Preprocessed)](https://drive.google.com/file/d/18_nlql4BbZtnxCnay-vYolcfS8XaXJ4z/view?usp=drive_link)

        https://drive.google.com/file/d/18_nlql4BbZtnxCnay-vYolcfS8XaXJ4z/view?usp=drive_link


The Preprocessed MirFlickr25k Dataset used here should be the outputs produced and combined from `../mirflickr25k-preprocessing` and `../image-augmentation` project directories.