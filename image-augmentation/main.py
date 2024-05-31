from motion_blur import v_motion_blur
from motion_blur import h_motion_blur
from perspective_transform import perspective_transform
from white_balance import white_balance
from gaussian_noise import gaussian_noise
from compression import jpeg_compression

from glob import glob
import matplotlib.pyplot as plt
import os
from natsort import natsorted
import random

images_dir = 'assets/stegastamp-encoded'
save_dir1 = 'assets/transformations/perspective-warp' 
save_dir2 = 'assets/transformations/blur'
save_dir3 = 'assets/transformations/color-shift'
save_dir4 = 'assets/transformations/noise'
save_dir5 = 'assets/transformations/jpeg-compressions'
# batch3.1 - perspective warp (im1-1250)
# batch3.2 - blur (im1251-2500)
# batch3.3 - color shift (im2501-3750)
# batch3.4 - noise (im3751-5000)
# batch3.5 - jpeg compression (im5001-6250)

def main():

    if not os.path.exists(save_dir1):
        os.makedirs(save_dir1)
    if not os.path.exists(save_dir2):
        os.makedirs(save_dir2)
    if not os.path.exists(save_dir3):
        os.makedirs(save_dir3)
    if not os.path.exists(save_dir4):
        os.makedirs(save_dir4)
    if not os.path.exists(save_dir5):
        os.makedirs(save_dir5)

    files_list = natsorted(glob(os.path.join(images_dir, '*.jpg')))

    # Perspective
    for filename in files_list[:1250]:
        im = plt.imread(filename)
        im = perspective_transform(im)

        save_name = filename.split('/')[-1].split('.')[0].split('im')[-1]
        save_name = 'im' + f'{int(save_name) + 25000}'
        plt.imsave(save_dir1 + '/' + save_name + '.jpg', im)
        print("Created " + save_dir1 + '/' + save_name + '.jpg')
    
    # Blur
    for filename in files_list[1250:2500]:
        im = plt.imread(filename)
        blur_direction = random.choice([h_motion_blur, v_motion_blur])
        im = blur_direction(im)

        save_name = filename.split('/')[-1].split('.')[0].split('im')[-1]
        save_name = 'im' + f'{int(save_name) + 25000}'
        plt.imsave(save_dir2 + '/' + save_name + '.jpg', im)
        print("Created " + save_dir2 + '/' + save_name + '.jpg')
    
    # Color Shift
    for filename in files_list[2500:3750]:
        im = plt.imread(filename)
        im = white_balance(im)

        save_name = filename.split('/')[-1].split('.')[0].split('im')[-1]
        save_name = 'im' + f'{int(save_name) + 25000}'
        plt.imsave(save_dir3 + '/' + save_name + '.jpg', im)
        print("Created " + save_dir3 + '/' + save_name + '.jpg')

    # Noise
    for filename in files_list[3750:5000]:
        im = plt.imread(filename)
        im = gaussian_noise(im)

        save_name = filename.split('/')[-1].split('.')[0].split('im')[-1]
        save_name = 'im' + f'{int(save_name) + 25000}'
        plt.imsave(save_dir4 + '/' + save_name + '.jpg', im)
        print("Created " + save_dir4 + '/' + save_name + '.jpg')

    # JPEG Compression
    for filename in files_list[5000:6250]:
        jpeg_compression(filename, save_dir5)
        

if __name__ == "__main__":
    main()