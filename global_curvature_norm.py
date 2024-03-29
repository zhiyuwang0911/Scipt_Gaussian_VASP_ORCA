import os
import glob
import numpy as np
import ase
from ase import io

xyz1 = glob.glob('opt/*.xyz')
xyz2 = glob.glob('original/*.xyz')

# global curvature
from matplotlib import pyplot as plt
fig, ax = plt.subplots(10,11) #parameter for plotting
fig.set_figheight(25)
fig.set_figwidth(25)
plt.subplots_adjust(hspace=0.5,wspace=0.5)
xyz1.sort()        
xyz2.sort()
all_avg=open('global_curvature_norm.dat','w')
for i in range(len(xyz1)):
    f=io.read(xyz1[i])
    #opt=f.arrays['positions'][list(f.arrays['numbers']).index(26)][2]
    g=io.read(xyz2[i])
    #org=g.arrays['positions'][list(g.arrays['numbers']).index(26)][2]
    #sub=opt-org
    num=f.arrays['numbers']
    coor=f.arrays['positions'][:,2]
    coor2=g.arrays['positions'][:,2]
    diff=coor2-coor 
    all_diff=[]
    for j in range(len(coor)):
        if num[j]!=26:
            all_diff.append(diff[j])
    norm_curv=np.mean(all_diff)
    all_avg.write('{} {}\n'.format(xyz1[i][4:12], norm_curv))
all_avg.close()
