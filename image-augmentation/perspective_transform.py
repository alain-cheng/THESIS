import cv2
import numpy as np

def perspective_transform(im=None, label=None):
    """
    Input Params:
        im - image directory
        label - label directory

    Returns:
        a tuple containing:
            im_warped - the warped image
            label_warped - the warped image label
    """

    # Randomize destination ranges
    #Top-Left
    x1 = np.random.randint(0, 51)
    y1 = np.random.randint(0, 51)
    #Top-Right
    x2 = np.random.randint(350, 401)
    y2 = np.random.randint(0, 51)
    #Bottom-Right
    x3 = np.random.randint(350, 401)
    y3 = np.random.randint(350, 401)
    #Bottom-Left
    x4 = np.random.randint(0, 51)
    y4 = np.random.randint(350, 401)

    # Perspective Warp 
    src = np.float32([[0,0], [400,0], [400,400], [0,400]])              # top-left, top-right, bottom-right, bottom-left
    dst = np.float32([[x1, y1], [x2, y2], [x3, y3], [x4, y4]])
    M = cv2.getPerspectiveTransform(src, dst)                           # Transformation Matrix
    im_warped = cv2.warpPerspective(im, M, (400,400))
    label_warped = cv2.warpPerspective(label, M, (400,400))

    return(im_warped, label_warped)