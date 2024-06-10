from PIL import Image, ImageEnhance
import cv2
import numpy as np
from glob import glob
from natsort import natsorted
import os
import random


backgrounds_dir = '../assets/DIV2K_train_HR'
overlays_dir = '../assets/mirflickr25k-preprocessed-annotated'
labels_dir = '../assets/mirflickr25k-preprocessed-annotated/labels'

im_save_dir1 = '../assets/synthesized'
lab_save_dir1 = '../assets/synthesized/labels'

save_dirs = {
    im_save_dir1: lab_save_dir1
}


def main():

    for im_dir, lab_dir in save_dirs.items():
        if not os.path.exists(im_dir):
            os.makedirs(im_dir)
        if not os.path.exists(lab_dir):
            os.makedirs(lab_dir)

    bg_files_list = natsorted(glob(os.path.join(backgrounds_dir, '*.png')))
    ovl_files_list = natsorted(glob(os.path.join(overlays_dir, '*.jpg')))
    lab_files_list = natsorted(glob(os.path.join(labels_dir, '*.jpg')))
    files_list = np.column_stack((ovl_files_list, lab_files_list))

    for ovl_file, lab_file in files_list[:, :]: ### ex. If it randomly stopped running at img6500.jpg, edit `files_list[6499:,:]` and run `python main.py` again

        # Randomly pick a background
        bg_file = bg_files_list[np.random.randint(0, len(bg_files_list))]
        #bg_file = bg_files_list[0]

        ## Open images
        bg = Image.open(bg_file)
        bg = bg.resize((2000, 2000), Image.Resampling.LANCZOS)
        bg_width, bg_height = bg.size
        overlay = Image.open(ovl_file).convert('RGBA')
        bg_black = Image.new('RGB', (bg_width, bg_height), (0, 0, 0))       # black bg is for label overlaying
        label = Image.open(lab_file).convert('RGBA')

        extra_flag = np.random.randint(0, 11) % 2
        if extra_flag == 0:
            extra_ovl_file, extra_lab_file = files_list[np.random.randint(10000, len(files_list[:, 0])), :] # skewing the rng to pick normal image more often
            extra_overlay = Image.open(extra_ovl_file).convert('RGBA')
            extra_label = Image.open(extra_lab_file).convert('RGBA')
        
        extra_extra_flag = random.choice([extra_flag, 0])
        if extra_extra_flag == 0:
            extra_extra_ovl_file, extra_extra_lab_file = files_list[np.random.randint(12450, len(files_list[:, 0])-4000), :] # skew towards perspective transform
            extra_extra_overlay = Image.open(extra_extra_ovl_file).convert('RGBA')
            extra_extra_label = Image.open(extra_extra_lab_file).convert('RGBA')


# Add augmentations to the images
        # Rotation
        randfloat = random.uniform(-3.0, 3.0)
        randfloat2 = random.uniform(-360, 360)
        r = np.random.randint(0, 255)
        g = np.random.randint(0, 255)
        b = np.random.randint(0, 255)
        bg = bg.rotate(randfloat, Image.Resampling.NEAREST, expand = False, fillcolor=(r,g,b)) # expand false so output img dimension is not affected
        overlay = overlay.rotate(randfloat2, expand = True)
        bg_black = bg_black.rotate(randfloat, expand = False)
        label = label.rotate(randfloat2, expand = True)
        
        if extra_flag == 0:
            randfloat2 = random.uniform(-360, 360)
            extra_overlay = extra_overlay.rotate(randfloat2, expand = True)
            extra_label = extra_label.rotate(randfloat2, expand = True) 

        if extra_extra_flag == 0:
             randfloat2 = random.uniform(-360, 360)
             extra_extra_overlay = extra_extra_overlay.rotate(randfloat2, expand = True)
             extra_extra_label = extra_extra_label.rotate(randfloat2, expand = True) 

        # Brightness
        bg = ImageEnhance.Brightness(bg).enhance(random.uniform(0.5, 1.5))  

# Generate a random coordinate on the bg
        rand_x = np.random.randint(0, bg_width+1-200)                       # Subtracting ~200 so the encoding doesnt go completely out-of-frame
        rand_y = np.random.randint(0, bg_height+1-200)
        randint = (rand_x, rand_y)

# Overlay mirflickr images onto div2k
        bg.paste(overlay, randint, mask=overlay)
        bg_black.paste(label, randint, mask=label)

        # Extra images
        if extra_flag == 0:
            rand_x = np.random.randint(0, bg_width+1-200)
            rand_y = np.random.randint(0, bg_height+1-200)
            randint = (rand_x, rand_y)
            bg.paste(extra_overlay, randint, mask=extra_overlay)
            bg_black.paste(extra_label, randint, mask=extra_label)
        
        if extra_extra_flag == 0:
            rand_x = np.random.randint(0, bg_width+1-200)
            rand_y = np.random.randint(0, bg_height+1-200)
            randint = (rand_x, rand_y)
            bg.paste(extra_extra_overlay, randint, mask=extra_extra_overlay)
            bg_black.paste(extra_extra_label, randint, mask=extra_extra_label)

        im_save_name = ovl_file.split('/')[-1].split('.')[0].split('im')[-1]
        lab_save_name = lab_file.split('/')[-1].split('.')[0].split('im')[-1].split('_')[0]
        im_save_name = 'im' + f'{int(im_save_name)}'
        lab_save_name = 'im' + f'{int(lab_save_name)}' + '_L'

        # Resize all outputs
        bg = bg.resize((1024, 1024), Image.Resampling.LANCZOS)
        bg_black = bg_black.resize((1024, 1024), Image.Resampling.LANCZOS)

# Save overlayed images
        bg.save(im_save_dir1 + '/' + im_save_name + '.jpg')
        bg_black.save(lab_save_dir1 + '/' + lab_save_name + '.jpg')
        print("Created " + im_save_dir1 + '/' + im_save_name + '.jpg')
        print("Created " + lab_save_dir1 + '/' + lab_save_name + '.jpg')


if __name__ == "__main__":
    main()
