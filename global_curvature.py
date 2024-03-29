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
for i in range(len(xyz1)):
    f=io.read(xyz1[i])
    #opt=f.arrays['positions'][list(f.arrays['numbers']).index(26)][2]
    g=io.read(xyz2[i])
    #org=g.arrays['positions'][list(g.arrays['numbers']).index(26)][2]
    sub=opt-org
    loc = open('global_curvature/{}.dat'.format(xyz1[i][4:12]), 'w')
    num=f.arrays['numbers']
    coor=f.arrays['positions'][:,2]
    coor2=g.arrays['positions'][:,2]
    diff=coor2-coor
    all_diff=[]
    for j in range(len(coor)):
        if num[j]!=26:
            loc.write('{}    {:.10f}\n'.format(num[j], diff[j]))
            all_diff.append(diff[j])
    loc.close()      # write substrate curvature to dat file.
    m=int(i/11)
    n=int((i-m*10)%11)
    ax[m,n].hist(all_diff)
    ax[m,n].set_title(xyz1[i][4:12])
plt.savefig('global_curvature.pdf') #plot histogram and save as pdf
