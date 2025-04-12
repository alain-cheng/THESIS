from PIL import Image, ImageEnhance, ImageFilter
import cv2
import csv
import numpy as np
from glob import glob
from natsort import natsorted
import os
import random

backgrounds_dir = '../assets/DIV2K_train_HR'

dataset_dir = '../assets/perturbed'
train_dir = '../assets/perturbed/train'
train_labels_dir = '../assets/perturbed/train_labels'
test_dir = '../assets/perturbed/test'
test_labels_dir = '../assets/perturbed/test_labels'
val_dir = '../assets/perturbed/val'
val_labels_dir = '../assets/perturbed/val_labels'

train_save_dir = '../assets/synthesized/train'
train_labels_save_dir = '../assets/synthesized/train_labels'
test_save_dir = '../assets/synthesized/test'
test_labels_save_dir = '../assets/synthesized/test_labels'
val_save_dir = '../assets/synthesized/val'
val_labels_save_dir = '../assets/synthesized/val_labels'

save_dirs = {
    train_save_dir: train_labels_save_dir,
    test_save_dir: test_labels_save_dir,
    val_save_dir: val_labels_save_dir
}

class_dict_data = [
    ["name", "r", "g", "b"],
    ["Embedded", 255, 255, 255],
    ["Background", 0, 0, 0]
]

def synthesize(backgrounds_dir, overlays_dir, labels_dir, im_save_dir, lab_save_dir):
    bg_files_list = natsorted(glob(os.path.join(backgrounds_dir, '*.png')))
    ovl_files_list = natsorted(glob(os.path.join(overlays_dir, '*.png')))
    lab_files_list = natsorted(glob(os.path.join(labels_dir, '*.png')))
    files_list = np.column_stack((ovl_files_list, lab_files_list))

    for ovl_file, lab_file in files_list[:, :]: ###
        # Randomly pick a background
        bg_file = bg_files_list[np.random.randint(0, len(bg_files_list))]

        ## Open images
        bg = Image.open(bg_file)
        bg = bg.resize((800, 800), Image.Resampling.LANCZOS)
        bg_width, bg_height = bg.size
        overlay = Image.open(ovl_file).convert('RGBA')
        bg_black = Image.new('RGB', (bg_width, bg_height), (0, 0, 0))       # black bg is for label overlaying
        label = Image.open(lab_file).convert('RGBA')

# Augmentations
        # Rotation
        #randfloat = random.uniform(-3.0, 3.0)
        randfloat2 = random.uniform(-360, 360)
        overlay = overlay.rotate(randfloat2, expand = True)
        #bg_black = bg_black.rotate(randfloat, expand = False)
        label = label.rotate(randfloat2, expand = True)

        # Brightness
        # bg = ImageEnhance.Brightness(bg).enhance(random.uniform(0.5, 1.5))  

# Compute a random coordinate on the bg
        rand_x = np.random.randint(0, bg_width+1-400)                       # Subtracting ~400 so the encoding doesnt go out-of-frame
        rand_y = np.random.randint(0, bg_height+1-400)
        randint = (rand_x, rand_y)

# Generate random color RGBA square
        rand_rgba = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
        sq_rgb = Image.new("RGBA", (800,800), rand_rgba)

# Overlay
        bg.paste(sq_rgb, (0,0), mask=sq_rgb)
        bg.paste(overlay, randint, mask=overlay)
        bg_black.paste(label, randint, mask=label)

        im_save_name = ovl_file.split('/')[-1].split('.')[0].split('im')[-1]
        lab_save_name = lab_file.split('/')[-1].split('.')[0].split('im')[-1]
        im_save_name = 'im' + f'{int(im_save_name)}'
        lab_save_name = 'im' + f'{int(lab_save_name)}'

        # Sharpen
        bg_black = bg_black.filter(ImageFilter.SHARPEN)
        
        # Resize all outputs
        bg = bg.resize((512, 512), Image.Resampling.LANCZOS)
        bg_black = bg_black.resize((512, 512), Image.Resampling.LANCZOS)

# Save overlayed images
        bg.save(im_save_dir + '/' + im_save_name + '.png')
        bg_black.save(lab_save_dir + '/' + lab_save_name + '.png')
        print("Created " + im_save_dir + '/' + im_save_name + '.png')
        print("Created " + lab_save_dir + '/' + lab_save_name + '.png')


def main():
    for im_dir, lab_dir in save_dirs.items():
        if not os.path.exists(im_dir):
            os.makedirs(im_dir)
        if not os.path.exists(lab_dir):
            os.makedirs(lab_dir)

    # Generate the csv file
    with open('../assets/synthesized/class_dict.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(class_dict_data)

    synthesize(backgrounds_dir, train_dir, train_labels_dir, train_save_dir, train_labels_save_dir)
    synthesize(backgrounds_dir, test_dir, test_labels_dir, test_save_dir, test_labels_save_dir)
    synthesize(backgrounds_dir, val_dir, val_labels_dir, val_save_dir, val_labels_save_dir)


if __name__ == "__main__":
    main()