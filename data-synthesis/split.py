import numpy as np
import matplotlib.pyplot as plt
#import pandas as pd
from natsort import natsorted
from glob import glob
import os
import shutil
from sklearn.model_selection import train_test_split


images_dir = "../assets/synthesized/*.jpg"
labels_dir = "../assets/synthesized/labels/*.jpg"

dataset_dir = "../assets/StegaStampV1"
train_dir = '../assets/StegaStampV1/train'
train_labels_dir = '../assets/StegaStampV1/train_labels'
val_dir = '../assets/StegaStampV1/val'
val_labels_dir = '../assets/StegaStampV1/val_labels'
test_dir = '../assets/StegaStampV1/test'
test_labels_dir = '../assets/StegaStampV1/test_labels'

split_dirs = {
    train_dir: train_labels_dir,
    val_dir: val_labels_dir,
    test_dir: test_labels_dir
}

# Train-Test-Val split for training BiSeNet V1
def main():
    im_files = natsorted(glob(images_dir))
    lab_files = natsorted(glob(labels_dir))

    data = np.column_stack((im_files, lab_files))

    train, test_val = train_test_split(data, train_size=0.7, test_size=0.3, random_state=42, shuffle=True)
    test, val = train_test_split(test_val, train_size=0.5, test_size=0.5)
    
    if not os.path.exists(dataset_dir):
        os.makedirs(dataset_dir)
    for im_dirs, lab_dirs in split_dirs.items():
        if not os.path.exists(im_dirs):
            os.makedirs(im_dirs)
        if not os.path.exists(lab_dirs):
            os.makedirs(lab_dirs)

    for im, lab in train:
        shutil.move(im, train_dir)
        shutil.move(lab, train_labels_dir)
    
    for im, lab in test:
        shutil.move(im, test_dir)
        shutil.move(lab, test_labels_dir)

    for im, lab in val:
        shutil.move(im, val_dir)
        shutil.move(lab, val_labels_dir)

if __name__ == "__main__":
    main()