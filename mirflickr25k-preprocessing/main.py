import os
from encode_image import encode_image

model = '../assets/saved_models/stegastamp_pretrained'

# the split MIRFLICKR dataset
train_dir = '../assets/MirFlickr/train'
test_dir = '../assets/MirFlickr/test'
val_dir = '../assets/MirFlickr/val'

dataset_save_dir = '../assets/stegastamp-encoded'

train_save_dir = '../assets/stegastamp-encoded/train'
train_labels_save_dir = '../assets/stegastamp-encoded/train_labels'

test_save_dir = '../assets/stegastamp-encoded/test'
test_labels_save_dir = '../assets/stegastamp-encoded/test_labels'

val_save_dir = '../assets/stegastamp-encoded/val'
val_labels_save_dir = '../assets/stegastamp-encoded/val_labels'

# directory to save the ground-truth messages
test_message_save_dir = '../assets/test_secrets' 

def main():
    if not os.path.exists(dataset_save_dir):
        os.makedirs(dataset_save_dir)

    # Train
    encode_image(model, images_dir=train_dir, save_dir=train_save_dir, label_save_dir=train_labels_save_dir)

    # Test
    encode_image(model, images_dir=test_dir, save_dir=test_save_dir, label_save_dir=test_labels_save_dir, message_save_dir=test_message_save_dir)

    # Val
    encode_image(model, images_dir=val_dir, save_dir=val_save_dir, label_save_dir=val_labels_save_dir)

    print("Finished.")

if __name__ == "__main__":
    main()