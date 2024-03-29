#check if Fe forms the shortest bond with 4 coordiate atoms and H atoms
#check1: if shorted 5 bond match
#check2: if any of other bond larger than 2.5 ang (highly distorted). if yes, copy xyz files to a subfolder

import os
import glob
import numpy as np
import shutil

final_folder_name = 'final_filter_structure'

# Create a new folder
os.makedirs(final_folder_name, exist_ok=True)

full_xyz = glob.glob('*xyz')
for file_name in full_xyz:
    print(file_name)
    bond_len = []
    with open(file_name, 'r') as file_xyz:
        for lines in file_xyz.readlines()[2:28]:
            data = lines.split()
            #print(data)
            if data[0] == "Fe":
                #print(data[0])
                x1,y1,z1 = map(float,data[1:4])
                print(x1,y1,z1)
    with open(file_name, 'r') as file_xyz:
        for lines in file_xyz.readlines()[2:28]:
            data = lines.split()
            print(data)
            if data[0] != "Fe":
                x2,y2,z2 = map(float,data[1:4])
                print(x2,y2,z2)
                bond_leng = np.sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)
                bond_len.append((data[0], bond_leng))
                #print(bond_leng,data[0])
    sorted_bond = sorted(bond_len, key=lambda y: y[1])
    print(sorted_bond)

    name_list = set([file_name[3],file_name[4],file_name[5],file_name[6],file_name[8]])
    print(name_list)
    list1=[]
    list2=[]
    count = 0
    for j in sorted_bond[0:5]:
        list1.append(j[0])
    set1= set(list1)
    if set1 == name_list:
        for i in sorted_bond[5:]:
            if float(i[1]) < 2.5:
                count += 1
        if count==0:
            shutil.copy(file_name, os.path.join(final_folder_name, file_name))
