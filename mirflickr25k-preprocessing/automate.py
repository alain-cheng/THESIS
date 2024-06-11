from encode_image import encode_image
from rescale_image import rescale_image
from generate_labels import generate_labels, generate_labels2

model = '../assets/saved_models/stegastamp_pretrained'
images_dir = '../assets/mirflickr25k/mirflickr'
save_dir1 = '../assets/stegastamp-encoded'
save_dir2 = '../assets/stegastamp-encoded'
    # save_dir1 - contains 50% (12.5k) samples to be resized to 400x400 and stegastamped
    # save_dir2 - contains 50% (12.5k) to be resized to 400x400

    # save_dir3 - contains 50% (6.25k) of out/batch1 and another 50% of out/batch2 to be augmented in ../image-augmentation 
    # (Needs to be manually created by copy-pasting images and labels from save_dir1)
        # (im1-6250) and (im12500-18750) are subject to all types of random perturbations

## Dataset V0: All just rescaled 400x400 (Outdated)
images_dir0_1 = 'mirflickr25k/mirflickr/batch1'
images_dir0_2 = 'mirflickr25k/mirflickr/batch2'
save_dir0 = 'out/batch0'

## Dataset V1.0: With text labels
def v_1_0():
    ## Outdated!
    encode_image(model, images_dir=images_dir0_1, save_dir=save_dir1)
    rescale_image(images_dir=images_dir0_2, save_dir=save_dir2)
    generate_labels(12500)
    generate_labels2(6250)
    pass


## Dataset V1.1: With annotation labels
def v_1_1():
    lim1 = (0, 12500)
    lim2 = (12500, 25001)
    encode_image(model, images_dir=images_dir, save_dir=save_dir1, limit=lim1)
    rescale_image(images_dir=images_dir, save_dir=save_dir2, limit=lim2)

def main():
    """
    Uncomment the Dataset version to generate for the project
    """
    #v_1_0()
    v_1_1()

    pass

if __name__ == "__main__":
    main()