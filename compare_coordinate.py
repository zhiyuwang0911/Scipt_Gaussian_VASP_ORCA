import glob
import os 
import numpy as np
import math


#with open('3z_fn4_c_TPSSh_opt.xyz','r') as xyz_file1:
    #coordinate1 = xyz_file1.readline()
 #   print(xyz_file1)

xyz_file1=open('3z_fn4_c_TPSSh_opt.xyz').readlines()

xyz_file2=open('3z_fn4_c_PBE_opt.xyz').readlines()

coordinate1 = xyz_file1[0][0:4].strip()
coordinate2 = xyz_file2[0][0:4].strip()

 
file = open('distance_of_atom.dat', 'w')
if int(coordinate1) == int(coordinate2):
    all_atom_diff=[]
    for i in range(len(xyz_file1[2:-2])):
        splitline = xyz_file1[2:-2][i].split()
        print(splitline)
        element_symbol = splitline[0]
        x1 = float(splitline[1])
        y1 = float(splitline[2])
        z1 = float(splitline[3])
        
        for j in range(len(xyz_file2[2:-2])):
            
            splitline2 = xyz_file2[2:-2][j].split()
            if i==j:
                element = splitline2[0]
                x2 = float(splitline2[1])
                y2 = float(splitline2[2])
                z2 = float(splitline2[3])
        atom_distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
        all_atom_diff.append(atom_distance)
        file.write('{} {:5f}\n'.format(element_symbol,atom_distance ))
    file.close()
average_atom_distance = np.mean(all_atom_diff)
print(average_atom_distance)
    #for i in atom_atom:
     ##   average = []
       # all_distance.append(average)
        #average_atom_distance = np.mean(all_distance)
        #print(average_atom_distance) 



    












