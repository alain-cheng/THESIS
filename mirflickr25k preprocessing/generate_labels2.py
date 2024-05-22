import os


save_dir1 = 'out/batch3/labels'

label1 = "StegaStamp"


def generate_labels2(n=6250):

    if not os.path.exists(save_dir1):
        os.makedirs(save_dir1)

    print("Generating Labels in " + save_dir1)
    for i in range(n):
        save_name1 = f"im{i+1}.txt"
        save_name2 = f"im{n+i+1}.txt"

        with open(os.path.join(save_dir1, save_name1), "w") as file:
            file.write(label1)
    
    print(f"{n} Labels Generated")