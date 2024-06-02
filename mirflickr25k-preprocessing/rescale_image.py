import numpy as np                  # type: ignore
import matplotlib.pyplot as plt     # type: ignore
from PIL import Image,ImageOps      # type: ignore
from glob import glob               # type: ignore
from natsort import natsorted       # type: ignore
from annotate import annotate       # type: ignore
import os


def rescale_image(image=None, images_dir=None, save_dir=None, size=(400,400), limit=None):
    
    if image is not None:
        files_list = [image]
    elif images_dir is not None:
        files_list = natsorted(glob(os.path.join(images_dir, '*.jpg'))) # edits
        files_list = [path.replace('\\', '/') for path in files_list] # edits
        if limit is not None:
            files_list = files_list[limit[0]:limit[1]]
    else:
        print('Missing input image')
        return

    if save_dir is not None:
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        for filename in files_list:
            image = Image.open(filename).convert("RGB")
            image = np.array(ImageOps.fit(image,size),dtype=np.float32)
            image /= 255.
            save_name = filename.split('/')[-1].split('.')[0]

            # Annotation RGB
            # StegaStamp (192, 0, 64)
            # Normal (64, 192, 128)
            annotate(color=(64, 192, 128), size=size, save_name=save_name, save_dir='../assets/stegastamp-encoded/labels')

            plt.imsave(save_dir + '/' + save_name + '.jpg', image)
            print("Created " + save_dir + '/' + save_name + '.jpg')

    print("Rescale Finished")
