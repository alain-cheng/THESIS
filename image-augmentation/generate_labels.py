import os


save_dir1 = 'assets/transformations/perspective-warp/labels'
save_dir2 = 'assets/transformations/blur/labels'
save_dir3 = 'assets/transformations/color-shift/labels'
save_dir4 = 'assets/transformations/noise/labels'
save_dir5 = 'assets/transformations/jpeg-compression/labels'

label1 = "StegaStamp"
label2 = "Normal"


def generate_labels():

    if not os.path.exists(save_dir1):
        os.makedirs(save_dir1)
    if not os.path.exists(save_dir2):
        os.makedirs(save_dir2)
    if not os.path.exists(save_dir3):
        os.makedirs(save_dir3)
    if not os.path.exists(save_dir4):
        os.makedirs(save_dir4)
    if not os.path.exists(save_dir5):
        os.makedirs(save_dir5)

    print("Generating Labels in " + save_dir1)
    print("Generating Labels in " + save_dir2)
    print("Generating Labels in " + save_dir3)
    print("Generating Labels in " + save_dir4)
    print("Generating Labels in " + save_dir5)

    for i in range(0, 1250):
        save_name = f"im{25000 + i + 1}.txt"
        with open(os.path.join(save_dir1, save_name), "w") as file:
            file.write(label1)
    
    print("Generated labels in " + save_dir1)

    for i in range(1250, 2500):
        save_name = f"im{25000 + i + 1}.txt"
        with open(os.path.join(save_dir2, save_name), "w") as file:
            file.write(label1)

    print("Generated labels in " + save_dir2)

    for i in range(2500, 3750):
        save_name = f"im{25000 + i + 1}.txt"
        with open(os.path.join(save_dir3, save_name), "w") as file:
            file.write(label1)

    print("Generated labels in " + save_dir3)

    for i in range(3750, 5000):
        save_name = f"im{25000 + i + 1}.txt"
        with open(os.path.join(save_dir4, save_name), "w") as file:
            file.write(label1)
    
    print("Generated labels in " + save_dir4)

    for i in range(5000, 6250):
        save_name = f"im{25000 + i + 1}.txt"
        with open(os.path.join(save_dir5, save_name), "w") as file:
            file.write(label1)

    print("Generated labels in " + save_dir5)

def main():
    generate_labels()

if __name__ == '__main__':
    main()