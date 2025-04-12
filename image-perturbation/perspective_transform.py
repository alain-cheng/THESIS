import cv2
import numpy as np

def perspective_transform(im, label):
    """
    Input Params:
        im - image directory
        label - label directory

    Returns:
        a tuple containing:
            im_warped - the warped image
            label_warped - the warped image label
    """

    im = cv2.cvtColor(im, cv2.COLOR_RGB2RGBA)
    label = cv2.cvtColor(label, cv2.COLOR_RGB2RGBA)

    # Randomize destination ranges give or take 40px // 10% of 400
    #Top-Left
    x1 = np.random.randint(0, 41)
    y1 = np.random.randint(0, 41)
    #Top-Right
    x2 = np.random.randint(360, 401)
    y2 = np.random.randint(0, 41)
    #Bottom-Right
    x3 = np.random.randint(360, 401)
    y3 = np.random.randint(360, 401)
    #Bottom-Left
    x4 = np.random.randint(0, 41)
    y4 = np.random.randint(360, 401)

    # Perspective Warp 
    src = np.float32([[0,0], [400,0], [400,400], [0,400]])              # top-left, top-right, bottom-right, bottom-left
    dst = np.float32([[x1, y1], [x2, y2], [x3, y3], [x4, y4]])
    M = cv2.getPerspectiveTransform(src, dst)                           # Transformation Matrix
    im_warped = cv2.warpPerspective(im, M, (400,400), borderValue=(0,0,0,0))
    label_warped = cv2.warpPerspective(label, M, (400,400), borderValue=(0,0,0,0))

    return(im_warped, label_warped)