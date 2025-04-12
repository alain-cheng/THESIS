from perspective_transform import perspective_transform

from glob import glob
import numpy as np
import matplotlib.pyplot as plt
import os
from natsort import natsorted
import random
from PIL import Image
import cv2

dataset_dir = '../assets/stegastamp-encoded'
train_dir = '../assets/stegastamp-encoded/train'
train_labels_dir = '../assets/stegastamp-encoded/train_labels'
test_dir = '../assets/stegastamp-encoded/test'
test_labels_dir = '../assets/stegastamp-encoded/test_labels'
val_dir = '../assets/stegastamp-encoded/val'
val_labels_dir = '../assets/stegastamp-encoded/val_labels'

dataset_save_dir = '../assets/perturbed'
train_save_dir = '../assets/perturbed/train'
train_labels_save_dir = '../assets/perturbed/train_labels'
test_save_dir = '../assets/perturbed/test'
test_labels_save_dir = '../assets/perturbed/test_labels'
val_save_dir = '../assets/perturbed/val'
val_labels_save_dir = '../assets/perturbed/val_labels'

def perturb(im_files, lab_files, im_save_dir, labels_save_dir):
    if not os.path.exists(im_save_dir):
        os.makedirs(im_save_dir)
    if not os.path.exists(labels_save_dir):
        os.makedirs(labels_save_dir)
    
    im_files_list = natsorted(glob(os.path.join(im_files, '*.png')))
    label_files_list = natsorted(glob(os.path.join(lab_files, '*.png')))
    
    files_list = np.column_stack((im_files_list, label_files_list))
    
    for filename in files_list[:, :]:
        im = Image.open(filename[0])
        im = np.array(im)
        label = Image.open(filename[1])
        label = np.array(label)
        
        im_save_name = filename[0].split('/')[-1].split('.')[0].split('im')[-1]
        label_save_name = filename[1].split('/')[-1].split('.')[0].split('im')[-1].split('_')[0]
        im_save_name = 'im' + f'{int(im_save_name)}'
        label_save_name = 'im' + f'{int(label_save_name)}'

        # Perspective Transform
        im, label = perspective_transform(im, label)
        
        cv2.imwrite(im_save_dir + '/' + im_save_name + '.png', cv2.cvtColor(im, cv2.COLOR_BGR2RGB))
        cv2.imwrite(labels_save_dir + '/' + label_save_name + '.png', label)

        print("Created " + im_save_dir + '/' + im_save_name + '.png')
        print("Created " + labels_save_dir + '/' + label_save_name + '.png')

def main():
    if not os.path.exists(dataset_save_dir):
        os.makedirs(dataset_save_dir)

    perturb(train_dir, train_labels_dir, train_save_dir, train_labels_save_dir)

    perturb(test_dir, test_labels_dir, test_save_dir, test_labels_save_dir)

    perturb(val_dir, val_labels_dir, val_save_dir, val_labels_save_dir)

if __name__ == "__main__":
    main()