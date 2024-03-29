#check if all the Z coordinate are all 0 or not. if it all 0, copy xyz to flat folder,otherwise, copy to unflat folder

import os
import glob
import shutil

def path():
    directory_path= input("Enter the directory have xyz files:")
    return directory_path

def check_structure_xyz(dir_path):
    new_folder1 = os.path.join(dir_path, 'flat_structure1')
    new_folder2 = os.path.join(dir_path, 'unflat_structure1')
    os.makedirs(new_folder1, exist_ok=True)
    os.makedirs(new_folder2, exist_ok=True)

    all_xyz = glob.glob(os.path.join(dir_path, "*xyz"))
    for filename in all_xyz:
        count = 0
        with open(filename, "r") as file_xyz:
            lines = file_xyz.readlines()
            total_atom = lines[0]
            all_line = lines[2:int(total_atom)+2]
            for line in all_line:
                iline = line.split()
                if iline[3] != '0.':
                    count += 1

            if count == 0:
                destination_folder = new_folder1
            else:
                destination_folder = new_folder2
                print(f'Unflat structure:{filename}')

            destination_path = os.path.join(destination_folder, os.path.basename(filename))
            if not os.path.exists(destination_path):
                shutil.copy(filename, destination_path)

def main():
    dir_path = path()
    copy_structure_to_folder = check_structure_xyz(dir_path)

if __name__ == "__main__":
    main()
