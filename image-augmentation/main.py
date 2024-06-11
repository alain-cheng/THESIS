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
import cv2

images_dir = '../assets/stegastamp-encoded'
labels_dir = '../assets/stegastamp-encoded/labels'

im_save_dir = '../assets/augmented'
label_save_dir = '../assets/augmented/labels'

def main():

    if not os.path.exists(im_save_dir):
        os.makedirs(im_save_dir)
    if not os.path.exists(label_save_dir):
        os.makedirs(label_save_dir)

    im_files_list = natsorted(glob(os.path.join(images_dir, '*.jpg')))
    label_files_list = natsorted(glob(os.path.join(labels_dir, '*.png')))
    files_list = np.column_stack((im_files_list, label_files_list))

    # Augment Images
    for filename in files_list[:, :]:
        im = plt.imread(filename[0])
        label = plt.imread(filename[1])

        # Noise
        im = gaussian_noise(im)
        # Perspective Transform
        im, label = perspective_transform(im, label)
        # Blur
        blur_direction = random.choice([h_motion_blur, v_motion_blur, gaussian_blur])
        im = blur_direction(im)
        # Color Shift
        im = white_balance(im)

        # JPEG Compression via OpenCV.imwrite & Save
        im = cv2.cvtColor(im, cv2.COLOR_RGB2BGR)

        im_save_name = filename[0].split('/')[-1].split('.')[0].split('im')[-1]
        label_save_name = filename[1].split('/')[-1].split('.')[0].split('im')[-1].split('_')[0]
        im_save_name = 'im' + f'{int(im_save_name)}'
        label_save_name = 'im' + f'{int(label_save_name)}'

        cv2.imwrite(im_save_dir + '/' + im_save_name + '.jpg', im, [int(cv2.IMWRITE_JPEG_QUALITY), np.random.randint(51, 100)])
        plt.imsave(label_save_dir + '/' + label_save_name + '_L' + '.png', label)

        print("Created " + im_save_dir + '/' + im_save_name + '.jpg')
        print("Created " + label_save_dir + '/' + label_save_name + '_L' + '.png')


if __name__ == "__main__":
    main()