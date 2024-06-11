import cv2
import numpy as np

def v_motion_blur(im):
    # Randomize Motion Blur Intensities between kernel size of 3 and 7
    k_size = np.random.randint(3,7)                               
    kernel_motblur = np.zeros((k_size,k_size))
    kernel_motblur[:, int((k_size - 1)/2)] = np.ones(k_size)
    kernel_motblur /= k_size
    kernel_motblur
    im_motblur = cv2.filter2D(im, -1, kernel_motblur)
    return(im_motblur)

def h_motion_blur(im):
    k_size = np.random.randint(3,7)                          
    kernel_motblur = np.zeros((k_size,k_size))
    kernel_motblur[int((k_size - 1)/2), :] = np.ones(k_size)
    kernel_motblur /= k_size
    kernel_motblur
    im_motblur = cv2.filter2D(im, -1, kernel_motblur)
    return(im_motblur)

def gaussian_blur(im):
    im_gaussian = cv2.GaussianBlur(im, (3, 3), np.random.randint(0,3))
    return(im_gaussian)