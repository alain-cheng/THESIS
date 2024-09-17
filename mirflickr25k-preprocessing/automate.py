import csv
import os
from encode_image import encode_image
from rescale_image import rescale_image

model = '../assets/saved_models/stegastamp_pretrained'

train_dir = '../assets/MirFlickr/train'
test_dir = '../assets/MirFlickr/test'
val_dir = '../assets/MirFlickr/val'

dataset_save_dir = '../assets/stegastamp-encoded'

train_save_dir = '../assets/stegastamp-encoded/train'
train_labels_save_dir = '../assets/stegastamp-encoded/train/labels'

test_save_dir = '../assets/stegastamp-encoded/test'
test_labels_save_dir = '../assets/stegastamp-encoded/test/labels'

val_save_dir = '../assets/stegastamp-encoded/val'
val_labels_save_dir = '../assets/stegastamp-encoded/val/labels'


class_dict_data = [
    ["name", "r", "g", "b"],
    ["StegaStamp", 192, 0, 64],
    ["Normal", 64, 192, 128],
    ["Unlabelled", 0, 0, 0]
]

def main():
    if not os.path.exists(dataset_save_dir):
        os.makedirs(dataset_save_dir)

    # Generate the csv file
    with open('../assets/stegastamp-encoded/class_dict.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(class_dict_data)

    # Train
    encode_image(model, images_dir=train_dir, save_dir=train_save_dir, label_save_dir=train_labels_save_dir)
    rescale_image(images_dir=train_dir, save_dir=train_save_dir, label_save_dir=train_labels_save_dir)

    # Test
    encode_image(model, images_dir=test_dir, save_dir=test_save_dir, label_save_dir=test_labels_save_dir)
    rescale_image(images_dir=test_dir, save_dir=test_save_dir, label_save_dir=test_labels_save_dir)

    # Val
    encode_image(model, images_dir=val_dir, save_dir=val_save_dir, label_save_dir=val_labels_save_dir)
    rescale_image(images_dir=val_dir, save_dir=val_save_dir, label_save_dir=val_labels_save_dir)

    print("Finished.")

if __name__ == "__main__":
    main()