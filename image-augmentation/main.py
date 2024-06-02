from motion_blur import v_motion_blur
from motion_blur import h_motion_blur
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

images_dir = '../assets/stegastamp-encoded'
labels_dir = '../assets/stegastamp-encoded/labels'

im_save_dir1 = '../assets/transformations/perspective-warp' 
label_save_dir1 = '../assets/transformations/perspective-warp/labels' 

im_save_dir2 = '../assets/transformations/blur'
label_save_dir2 = '../assets/transformations/blur/labels'

im_save_dir3 = '../assets/transformations/color-shift'
label_save_dir3 = '../assets/transformations/color-shift/labels'

im_save_dir4 = '../assets/transformations/noise'
label_save_dir4 = '../assets/transformations/noise/labels'

im_save_dir5 = '../assets/transformations/jpeg-compressions'
label_save_dir5 = '../assets/transformations/jpeg-compressions/labels'

# Images to be Augmented:
    # perspective warp (im1-1250)
    # blur (im1251-2500)
    # color shift (im2501-3750)
    # noise (im3751-5000)
    # jpeg compression (im5001-6250)

def main():

    if not os.path.exists(im_save_dir1):
        os.makedirs(im_save_dir1)
    if not os.path.exists(label_save_dir1):
        os.makedirs(label_save_dir1)
    if not os.path.exists(im_save_dir2):
        os.makedirs(im_save_dir2)
    if not os.path.exists(label_save_dir2):
        os.makedirs(label_save_dir2)
    if not os.path.exists(im_save_dir3):
        os.makedirs(im_save_dir3)
    if not os.path.exists(label_save_dir3):
        os.makedirs(label_save_dir3)
    if not os.path.exists(im_save_dir4):
        os.makedirs(im_save_dir4)
    if not os.path.exists(label_save_dir4):
        os.makedirs(label_save_dir4)
    if not os.path.exists(im_save_dir5):
        os.makedirs(im_save_dir5)
    if not os.path.exists(label_save_dir5):
        os.makedirs(label_save_dir5)

    im_files_list = natsorted(glob(os.path.join(images_dir, '*.jpg')))
    label_files_list = natsorted(glob(os.path.join(labels_dir, '*.jpg')))
    files_list = np.column_stack((im_files_list, label_files_list))

    # Perspective
    for filename in files_list[:1, :]:
        im = plt.imread(filename[0])
        label = plt.imread(filename[1])
        im, label = perspective_transform(im, label)

        im_save_name = filename[0].split('/')[-1].split('.')[0].split('im')[-1]
        label_save_name = filename[1].split('/')[-1].split('.')[0].split('im')[-1].split('_')[0]
        im_save_name = 'im' + f'{int(im_save_name) + 25000}'
        label_save_name = 'im' + f'{int(label_save_name) + 25000}'

        plt.imsave(im_save_dir1 + '/' + im_save_name + '.jpg', im)
        plt.imsave(label_save_dir1 + '/' + label_save_name + '_L' + '.jpg', label)
        print("Created " + im_save_dir1 + '/' + im_save_name + '.jpg')
        print("Created " + label_save_dir1 + '/' + label_save_name + '_L' + '.jpg')
    
    # Blur
    for filename in files_list[1250:2500, :]:
        im = plt.imread(filename[0])
        label = plt.imread(filename[1])
        # Randomly pick between horizontal or vertical motion blur
        blur_direction = random.choice([h_motion_blur, v_motion_blur])
        im = blur_direction(im)

        im_save_name = filename[0].split('/')[-1].split('.')[0].split('im')[-1]
        label_save_name = filename[1].split('/')[-1].split('.')[0].split('im')[-1].split('_')[0]
        im_save_name = 'im' + f'{int(im_save_name) + 25000}'
        label_save_name = 'im' + f'{int(label_save_name) + 25000}'

        plt.imsave(im_save_dir2 + '/' + im_save_name + '.jpg', im)
        plt.imsave(label_save_dir2 + '/' + label_save_name + '_L' + '.jpg', label)
        print("Created " + im_save_dir2 + '/' + im_save_name + '.jpg')
        print("Created " + label_save_dir2 + '/' + label_save_name + '_L' + '.jpg')
    
    # Color Shift
    for filename in files_list[2500:3750, :]:
        im = plt.imread(filename[0])
        label = plt.imread(filename[1])
        im = white_balance(im)

        im_save_name = filename[0].split('/')[-1].split('.')[0].split('im')[-1]
        label_save_name = filename[1].split('/')[-1].split('.')[0].split('im')[-1].split('_')[0]
        im_save_name = 'im' + f'{int(im_save_name) + 25000}'
        label_save_name = 'im' + f'{int(label_save_name) + 25000}'

        plt.imsave(im_save_dir3 + '/' + im_save_name + '.jpg', im)
        plt.imsave(label_save_dir3 + '/' + label_save_name + '_L' + '.jpg', label)
        print("Created " + im_save_dir3 + '/' + im_save_name + '.jpg')
        print("Created " + label_save_dir3 + '/' + label_save_name + '_L' + '.jpg')

    # Noise
    for filename in files_list[3750:5000, :]:
        im = plt.imread(filename[0])
        label = plt.imread(filename[1])
        im = gaussian_noise(im)

        im_save_name = filename[0].split('/')[-1].split('.')[0].split('im')[-1]
        label_save_name = filename[1].split('/')[-1].split('.')[0].split('im')[-1].split('_')[0]
        im_save_name = 'im' + f'{int(im_save_name) + 25000}'
        label_save_name = 'im' + f'{int(label_save_name) + 25000}'
        
        plt.imsave(im_save_dir4 + '/' + im_save_name + '.jpg', im)
        plt.imsave(label_save_dir4 + '/' + label_save_name + '_L' + '.jpg', label)
        print("Created " + im_save_dir4 + '/' + im_save_name + '.jpg')
        print("Created " + label_save_dir4 + '/' + label_save_name + '_L' + '.jpg')

    # JPEG Compression
    for filename in files_list[5000:6250, :]:
        jpeg_compression(filename[0], im_save_dir5)
        label = plt.imread(filename[1])

        label_save_name = filename[1].split('/')[-1].split('.')[0].split('im')[-1].split('_')[0]
        label_save_name = 'im' + f'{int(label_save_name) + 25000}'
        plt.imsave(label_save_dir5 + '/' + label_save_name + '_L' + '.jpg', label)
        print("Created " + label_save_dir5 + '/' + label_save_name + '_L' + '.jpg')

if __name__ == "__main__":
    main()