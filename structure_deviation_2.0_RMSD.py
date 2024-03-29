#calculate the RMSD between original and relaxed structure
import os
import glob
import numpy as np

directory1 = '/blue/mingjieliu/wangzhiyu/funtional/small_flake/small_325/original/'
directory2 = '/blue/mingjieliu/wangzhiyu/funtional/small_flake/small_325/opt_325/'
new_filename='result.csv'


new_file = open(new_filename,'w')
os.chdir(directory1)
all_xyz = glob.glob('*xyz')
all_xyz.sort()
#print(all_xyz)

for i in all_xyz:
    print(i)
    list1 = []
    list2 = []
    with open(i,'r') as file1, open(directory2+i[:-4]+'_opt.xyz','r') as file2:
        for line1,line2 in zip(file1.readlines()[2:29],file2.readlines()[2:29]):
            part1 = line1.split()
            part2 = line2.split()
            #print(part1)
            x1,y1,z1 = map(float,part1[1:4])
            x2,y2,z2 = map(float,part2[1:4])
            #print(file1,file2)
            print(x1,y1,z1)
            #print(x2,y2,z2)
            list1.append([x1,y1,z1])
            list2.append([x2,y2,z2])
    all_dev = []
    for j in range(len(list1)):
        dev = np.sqrt((list1[j][0]-list2[j][0])**2+(list1[j][1]-list2[j][1])**2+(list1[j][2]-list2[j][2])**2)
        all_dev.append(dev)
    avg_dev = np.mean(all_dev)
    new_file.write('{},  {}\n'.format(i[:-4], avg_dev))
new_file.close()

