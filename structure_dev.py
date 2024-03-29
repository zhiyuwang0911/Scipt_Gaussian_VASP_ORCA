#calculate the structure deviation between unrelax and relax structure by mean absolute error

import os 
import glob as glob
import math
import numpy as np
directory1 = '/blue/mingjieliu/wangzhiyu/funtional/small_flake/small_325/original_h'
directory2 = '/blue/mingjieliu/wangzhiyu/funtional/small_flake/small_325/opt_325_h/'

new_f=open('result_325_h.dat','w')
os.chdir(directory1)
all_xyz = glob.glob('*xyz')
all_xyz.sort()

#new_f=open('result.dat','w')
for i in all_xyz:
    list1=[]
    list2=[]
    print(i)
    file1=open(i,'r')
    file2=open(directory2+i[:-4] + '_opt.xyz', 'r')
    for line1 in file1.readlines()[2:]:
        part1 = line1.split()
        x1 = float(part1[1])
        y1 = float(part1[2])
        z1 = float(part1[3])
        list1.append([x1,y1,z1])
        print(part1,x1,y1,z1)
    for line2 in file2.readlines()[2:-2]:
        part2 = line2.split()
        x2 = float(part2[1])
        y2 = float(part2[2])
        z2 = float(part2[3])
        list2.append([x2,y2,z2])
        print(part2,x2,y2,z2)        
    all_dev=[]
    for ind in range(len(list1)):
        dev=np.sqrt((list1[ind][0]-list2[ind][0])**2+(list1[ind][1]-list2[ind][1])**2+(list1[ind][2]-list2[ind][2])**2)
        all_dev.append(dev)
        avg_dev=np.mean(all_dev)
    new_f.write('{} {}\n'.format(i[:-4],avg_dev))
new_f.close()


