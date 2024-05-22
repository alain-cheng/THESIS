import os


save_dir1 = 'out/batch1/labels'
save_dir2 = 'out/batch2/labels'

label1 = "StegaStamp"
label2 = "Normal"


def generate_labels(n=12500):

    if not os.path.exists(save_dir1):
        os.makedirs(save_dir1)
    if not os.path.exists(save_dir2):
        os.makedirs(save_dir2)

    print("Generating Labels in " + save_dir1)
    print("Generating Labels in " + save_dir2)

    for i in range(n):
        save_name1 = f"im{i+1}.txt"
        save_name2 = f"im{n+i+1}.txt"

        with open(os.path.join(save_dir1, save_name1), "w") as file:
            file.write(label1)
        with open(os.path.join(save_dir2, save_name2), "w") as file:
            file.write(label2)
    
    print(f"{n*2} Labels Generated")