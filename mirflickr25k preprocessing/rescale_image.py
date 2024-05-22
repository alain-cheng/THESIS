import cv2
import matplotlib.pyplot as plt
import pandas as pd
from glob import glob
import os

from natsort import natsorted

def rescale_image(image=None, images_dir=None, save_dir=None, x_size=400, y_size=400):
    
    if image is not None:
        files_list = [image]
    elif images_dir is not None:
        files_list = natsorted(glob(os.path.join(images_dir, '*.jpg'))) # edits
        files_list = [path.replace('\\', '/') for path in files_list] # edits
    else:
        print('Missing input image')
        return

    if save_dir is not None:
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        for filename in files_list:

            im = plt.imread(filename)

            save_name = filename.split('/')[-1].split('.')[0]

            im = cv2.resize(im, (x_size, y_size), interpolation=cv2.INTER_LINEAR)

            plt.imsave(save_dir + '/' + save_name + '.jpg', im)
            print("Created " + save_dir + '/' + save_name + '.jpg')

    print("Rescale Finished")
