from blur import v_motion_blur, h_motion_blur, gaussian_blur
from perspective_transform import perspective_transform
from white_balance import white_balance
from gaussian_noise import gaussian_noise
from compression import jpeg_compression

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
train_labels_dir = '../assets/stegastamp-encoded/train/labels'
test_dir = '../assets/stegastamp-encoded/test'
test_labels_dir = '../assets/stegastamp-encoded/test/labels'
val_dir = '../assets/stegastamp-encoded/val'
val_labels_dir = '../assets/stegastamp-encoded/val/labels'

dataset_save_dir = '../assets/perturbed'
train_save_dir = '../assets/perturbed/train'
train_labels_save_dir = '../assets/perturbed/train/labels'
test_save_dir = '../assets/perturbed/test'
test_labels_save_dir = '../assets/perturbed/test/labels'
val_save_dir = '../assets/perturbed/val'
val_labels_save_dir = '../assets/perturbed/val/labels'

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
        label = plt.imread(filename[1])
        
        # Noise
        im = gaussian_noise(im)
        # Blur
        blur_direction = random.choice([h_motion_blur, v_motion_blur, gaussian_blur])
        im = blur_direction(im)
        # Color Shift
        im = white_balance(im)
        
        im_save_name = filename[0].split('/')[-1].split('.')[0].split('im')[-1]
        label_save_name = filename[1].split('/')[-1].split('.')[0].split('im')[-1].split('_')[0]
        im_save_name = 'im' + f'{int(im_save_name)}'
        label_save_name = 'im' + f'{int(label_save_name)}'
        
        # JPEG Compression via PIL
        im_pil = Image.fromarray(im)
        if im_pil.mode == 'RGBA':
            im_pil = im_pil.convert('RGB')
        im_buffer = 'temp.jpg'
        im_pil.save(im_buffer, 'JPEG', quality=np.random.randint(51, 100))
        im = Image.open(im_buffer).convert('RGBA')
        im = cv2.cvtColor(np.array(im), cv2.COLOR_RGBA2BGRA) # PIL to CV2

        # Perspective Transform
        im, label = perspective_transform(im, label)
        
        cv2.imwrite(im_save_dir + '/' + im_save_name + '.png', im)
        plt.imsave(labels_save_dir + '/' + label_save_name + '_L' + '.png', label)

        print("Created " + im_save_dir + '/' + im_save_name + '.png')
        print("Created " + labels_save_dir + '/' + label_save_name + '_L' + '.png')

def main():
    if not os.path.exists(dataset_save_dir):
        os.makedirs(dataset_save_dir)

    perturb(train_dir, train_labels_dir, train_save_dir, train_labels_save_dir)

    perturb(test_dir, test_labels_dir, test_save_dir, test_labels_save_dir)

    perturb(val_dir, val_labels_dir, val_save_dir, val_labels_save_dir)

if __name__ == "__main__":
    main()