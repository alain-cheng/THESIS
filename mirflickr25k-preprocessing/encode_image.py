import bchlib                                                   # type: ignore
from glob import glob
import os
from PIL import Image,ImageOps                                  # type: ignore
import numpy as np                                              # type: ignore
import tensorflow as tf                                         # type: ignore
import tensorflow.contrib.image                                 # type: ignore
from tensorflow.python.saved_model import tag_constants         # type: ignore
from tensorflow.python.saved_model import signature_constants   # type: ignore

import random
import string
from natsort import natsorted                                   # type: ignore
from annotate import annotate

BCH_POLYNOMIAL = 137
BCH_BITS = 5

'''
This function was taken from StegaStamp's encode_image.py and modified for 
the purpose of dataset preprocessing.
'''
def encode_image(model, image=None, images_dir=None, save_dir=None, secret='1234567', limit=None):

    # Edits: Removed all instances of args + Converted encode_image.py to a function

    if image is not None:
        files_list = [image]
    elif images_dir is not None:
        files_list = natsorted(glob(os.path.join(images_dir, '*.jpg'))) # edits
        files_list = [path.replace('\\', '/') for path in files_list]   # edits
        if limit is not None:
            files_list = files_list[limit[0]:limit[1]]
    else:
        print('Missing input image')
        return

    sess = tf.InteractiveSession(graph=tf.Graph())

    model = tf.saved_model.loader.load(sess, [tag_constants.SERVING], model)

    input_secret_name = model.signature_def[signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY].inputs['secret'].name
    input_image_name = model.signature_def[signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY].inputs['image'].name
    input_secret = tf.get_default_graph().get_tensor_by_name(input_secret_name)
    input_image = tf.get_default_graph().get_tensor_by_name(input_image_name)

    output_stegastamp_name = model.signature_def[signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY].outputs['stegastamp'].name
    output_residual_name = model.signature_def[signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY].outputs['residual'].name
    output_stegastamp = tf.get_default_graph().get_tensor_by_name(output_stegastamp_name)
    output_residual = tf.get_default_graph().get_tensor_by_name(output_residual_name)

    width = 400
    height = 400

    bch = bchlib.BCH(BCH_POLYNOMIAL, BCH_BITS)

    if save_dir is not None:
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        size = (width, height)
        for filename in files_list:
            # Edits: Randomizes a string of 7 characters
            secret = ''.join(
                random.choices(
                    string.ascii_letters + 
                    string.digits +
                    string.punctuation, 
                k = 7))
            
            # Edits: Repositioned this code segment into the for loop
            if len(secret) > 7:
                print('Error: Can only encode 56bits (7 characters) with ECC')
                return
            data = bytearray(secret + ' '*(7-len(secret)), 'utf-8')
            ecc = bch.encode(data)
            packet = data + ecc
            packet_binary = ''.join(format(x, '08b') for x in packet)
            secret = [int(x) for x in packet_binary]
            secret.extend([0,0,0,0])

            image = Image.open(filename).convert("RGB")
            image = np.array(ImageOps.fit(image,size),dtype=np.float32)
            image /= 255.

            feed_dict = {input_secret:[secret],
                         input_image:[image]}

            hidden_img, residual = sess.run([output_stegastamp, output_residual],feed_dict=feed_dict)

            rescaled = (hidden_img[0] * 255).astype(np.uint8)
            #raw_img = (image * 255).astype(np.uint8)
            #residual = residual[0]+.5
            #residual = (residual * 255).astype(np.uint8)

            save_name = filename.split('/')[-1].split('.')[0]
            im = Image.fromarray(np.array(rescaled))
            im.save(save_dir + '/' + save_name + '.jpg') # edits
            print("Created " + save_dir + '/' + save_name + '.jpg') # edits

            # Annotation RGB
            # StegaStamp (192, 0, 64)
            # Normal (64, 192, 128)
            annotate(color=(192, 0, 64), size=size, save_name=save_name, save_dir='out/batch1/labels')

            #im = Image.fromarray(np.squeeze(np.array(residual)))
            #im.save(save_dir + '/residuals'+'/'+save_name+'.png') # edits

    print("Encoding Finished")