import cv2
import numpy as np

def gaussian_noise(im):
    mean = 0
    std = np.random.uniform(0.2, 0.6)
    noise = np.random.normal(mean, std, im.shape).astype(np.uint8)
    im_noise = cv2.add(im, noise)
    return(im_noise)