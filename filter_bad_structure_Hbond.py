#filter structure if H atoms forms the shortest bond with Fe, if so, copy xzy to new folder

import os
import glob
import numpy as np
import shutil

new_folder_name = 'filter_structure'

# Create a new folder
os.makedirs(new_folder_name, exist_ok=True)

all_xyz = glob.glob('*xyz')
for file_name in all_xyz:
    bond_lengths = []
    print(file_name)
    with open(file_name, 'r') as file_xyz:
        lines = file_xyz.readlines()
        x1,y1,z1 = map(float,lines[27].split()[1:4])  # Last atom's coordinates
        print(x1,y1,z1)

        # Iterate over atoms in the file
        for line in lines[2:27]:
            atom_data = line.split()
            x2,y2,z2 = map(float,atom_data[1:4])

            #print(x2,y2,z2)
            bond_length = np.sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)
            bond_lengths.append((atom_data[0], bond_length))

        bond_lengths.sort(key=lambda x: x[1])
        print(len(bond_lengths))
        #with open(file_name[:-4] + '_bl.csv', 'w') as new_file:
            #for atom, bond_length in bond_lengths:
                #new_file.write("{}, {}\n".format(atom, bond_length))
        print(bond_lengths)

        if bond_lengths[0][0] == 'Fe':
            shutil.copy(file_name, os.path.join(new_folder_name, file_name))i
