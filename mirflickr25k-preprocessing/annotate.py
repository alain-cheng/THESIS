import os
from PIL import Image

save_dir = None

def annotate(color=(0, 0, 0), size=(400, 400), save_name=None, save_dir=None):
    """
    Input Params:
        color - a tuple containing three integers corresponding to RGB values
        size - a tuple containing the output width and height image
        save_name - a string; image name
        save_dir - a string; the output directory of the annotation
    """
    # Note: were actually just creating solid 400x400 blocks of color

    if save_name is not None:
        if save_dir is not None:
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)
        
            label = Image.new('RGB', (size[0],size[1]), (color[0], color[1], color[2]))
            label.save(save_dir + '/' + save_name + '_L' + '.png')
        else:
            print("save_dir is not defined")
    else:
        print("save_name is not defined")
    