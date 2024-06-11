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

im_save_dir1 = '../assets/synthesized-v2'
lab_save_dir1 = '../assets/synthesized-v2/labels'

save_dirs = {
    im_save_dir1: lab_save_dir1
}

## main-v2 is for generating data for BiSeNet-V2
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

    count = 0
    for ovl_file, lab_file in files_list[:, :]: ###

        # Flag
        if count < 12500:
            flag = "StegaStamp"
        elif count >= 12500 and count < 25000:
            flag = "Normal"
        else:
            flag = "StegaStamp"

        # Randomly pick a background
        bg_file = bg_files_list[np.random.randint(0, len(bg_files_list))]

        ## Open images
        bg = Image.open(bg_file)
        bg = bg.resize((1000, 1000), Image.Resampling.LANCZOS)
        bg_width, bg_height = bg.size
        overlay = Image.open(ovl_file).convert('RGBA')
        bg_black_s = Image.new('RGB', (bg_width, bg_height), (0, 0, 0))       # black bg is for label overlaying
        bg_black_n = bg_black_s.copy()
        label = Image.open(lab_file).convert('RGBA')

        extra_flag = np.random.randint(0, 11) % 2
        if extra_flag == 0:
            extra_ovl_file, extra_lab_file = files_list[np.random.randint(25000, 26251), :] # 2nd image is guaranteed StegaStamp with transformation
            extra_overlay = Image.open(extra_ovl_file).convert('RGBA')
            extra_label = Image.open(extra_lab_file).convert('RGBA')
        
        extra_extra_flag = random.choice([extra_flag, 0])
        if extra_extra_flag == 0:
            extra_extra_ovl_file, extra_extra_lab_file = files_list[np.random.randint(12500, 25000), :] # 3rd image is guaranteed Normal image
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
        bg_black_s = bg_black_s.rotate(randfloat, expand = False)
        bg_black_n = bg_black_n.rotate(randfloat, expand = False)
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

# Overlay mirflickr images onto div2k

        # Extra images go first if any
        if extra_flag == 0:
            rand_x = np.random.randint(0, bg_width+1-400)
            rand_y = np.random.randint(0, bg_height+1-400)
            randint = (rand_x, rand_y)
            bg.paste(extra_overlay, randint, mask=extra_overlay)
            bg_black_s.paste(extra_label, randint, mask=extra_label)
        
        if extra_extra_flag == 0:
            rand_x = np.random.randint(0, bg_width+1-400)
            rand_y = np.random.randint(0, bg_height+1-400)
            randint = (rand_x, rand_y)
            bg.paste(extra_extra_overlay, randint, mask=extra_extra_overlay)
            bg_black_n.paste(extra_extra_label, randint, mask=extra_extra_label)

        rand_x = np.random.randint(0, bg_width+1-400)                       # Subtracting ~200 so the encoding doesnt go completely out-of-frame
        rand_y = np.random.randint(0, bg_height+1-400)
        randint = (rand_x, rand_y)
        bg.paste(overlay, randint, mask=overlay)
        if flag == "StegaStamp":
            bg_black_s.paste(label, randint, mask=label)
        else:
            bg_black_n.paste(label, randint, mask=label)

        im_save_name = ovl_file.split('/')[-1].split('.')[0].split('im')[-1]
        lab_save_name = lab_file.split('/')[-1].split('.')[0].split('im')[-1].split('_')[0]
        im_save_name = 'im' + f'{int(im_save_name)}'
        lab_save_name = 'im' + f'{int(lab_save_name)}' + '_L'

        # Convert labels to full bnw
        thresh = 25
        fn = lambda x : 255 if x > thresh else 0
        bg_black_s = bg_black_s.convert('L').point(fn, mode='1')
        bg_black_n = bg_black_n.convert('L').point(fn, mode='1')

        # Resize all outputs
        bg = bg.resize((800, 800), Image.Resampling.LANCZOS)
        bg_black_s = bg_black_s.resize((800, 800), Image.Resampling.LANCZOS)
        bg_black_n = bg_black_n.resize((800, 800), Image.Resampling.LANCZOS)

# Save overlayed images
        bg.save(im_save_dir1 + '/' + im_save_name + '.png')
        if flag == "StegaStamp" or extra_flag == 0:
            bg_black_s.save(lab_save_dir1 + '/' + lab_save_name + '_StegaStamp' + '.png')
            print("Created " + lab_save_dir1 + '/' + lab_save_name + '_StegaStamp' + '.png')
        if flag == "Normal" or extra_extra_flag == 0:
            bg_black_n.save(lab_save_dir1 + '/' + lab_save_name + '_Normal' + '.png')
            print("Created " + lab_save_dir1 + '/' + lab_save_name + '_Normal' + '.png')
        print("Created " + im_save_dir1 + '/' + im_save_name + '.jpg')

        # Increment count
        count += 1

if __name__ == "__main__":
    main()
