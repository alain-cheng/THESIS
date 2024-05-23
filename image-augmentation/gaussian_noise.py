import cv2
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def gaussian_noise(im):
    mean = 0
    std = np.random.uniform(0.5, 1.0)

    noise = np.random.normal(mean, std, im.shape).astype(np.uint8)
    im_noise = cv2.add(im, noise)

    return(im_noise)