# Train-Test-Val split
import numpy as np
import matplotlib.pyplot as plt
from natsort import natsorted
from glob import glob
import os
import shutil
from sklearn.model_selection import train_test_split


images_dir = '../assets/mirflickr'
    # Do the command below after unzipping the downloaded mirflickr dataset for the first time before running the code:
        # find . -type f ! -name '*.jpg' -delete

dataset_dir = '../assets/MirFlickr'
train_dir = '../assets/MirFlickr/train'
test_dir = '../assets/MirFlickr/test'
val_dir = '../assets/MirFlickr/val'

def main():
    im_files = natsorted(glob(os.path.join(images_dir, '*')))
    im_files = im_files[0:7250]

    # Partition to 70-15-15
    train, test_val = train_test_split(im_files, train_size=0.7, test_size=0.3, random_state=42, shuffle=True)
    test, val = train_test_split(test_val, train_size=0.5, test_size=0.5)
    
    if not os.path.exists(dataset_dir):
        os.makedirs(dataset_dir)
    if not os.path.exists(train_dir):
        os.makedirs(train_dir)
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)
    if not os.path.exists(val_dir):
        os.makedirs(val_dir)

    for im in train:
        shutil.move(im, train_dir)
    
    print('Train Split Done.')
    
    for im in test:
        shutil.move(im, test_dir)
    
    print('Test Split Done.')

    for im in val:
        shutil.move(im, val_dir)

    print('Train-Test-Val Split finished.')

if __name__ == "__main__":
    main()