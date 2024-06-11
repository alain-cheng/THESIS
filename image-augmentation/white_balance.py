import numpy as np
import cv2

def white_balance(im):
    avg = np.mean(im)

    # Randomize wb scaling
    r = np.random.uniform(1.0, 2.0)
    g = np.random.uniform(1.0, 2.0)
    b = np.random.uniform(1.0, 2.0)
    scale = np.array([r,g,b])

    # im_wb = im * scale
    im_wb = cv2.multiply(im, scale)
    im_wb = np.clip(im_wb, 0, 255).astype(np.uint8)

    return(im_wb)