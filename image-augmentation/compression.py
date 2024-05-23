import cv2
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def jpeg_compression(im_file, save_dir='out/batch3.5'):

    im = plt.imread(im_file)

    save_name = im_file.split('/')[-1].split('.')[0].split('im')[-1]
    save_name = 'im' + f'{int(save_name) + 25000}'
    
    im_bgr = cv2.cvtColor(im, cv2.COLOR_RGB2BGR)

    cv2.imwrite(save_dir + '/' + save_name + '.jpg', im_bgr, [int(cv2.IMWRITE_JPEG_QUALITY), np.random.randint(50,101)])
    print("Created" + save_dir + '/' + save_name + '.jpg')