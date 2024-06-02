from PIL import Image
from glob import glob
from natsort import natsorted
import os

backgrounds_dir = '../assets/DIV2K_train_HR'
overlays_dir = '../assets/mirflickr25k-preprocessed-annotated'
labels_dir = '../assets/mirflickr25k-preprocessed-annotated/labels'

# TODO: complete functionalities
def main():
    bg_files_list = natsorted(glob(os.path.join(backgrounds_dir, '*.png')))
    ovl_files_list = natsorted(glob(os.path.join(overlays_dir, '*.jpg')))

    bg_file = bg_files_list[0]
    ovl_file = ovl_files_list[0]

    bg = Image.open(bg_file)
    ovl = Image.open(ovl_file)

    bg.paste(ovl, (0,0))

    bg.show()

if __name__ == "__main__":
    main()