import glob
import os
import numpy as np
direc=os.getcwd().split('/')[-1]
xyz=np.loadtxt(direc+'.com', skiprows=8, dtype=str)
dat=np.loadtxt('ACF.dat',skiprows=2, max_rows=len(xyz), dtype=str)
everything=np.column_stack([xyz,dat])
for col in everything:
    if col[0]=='Fe':
        charge=float(8-float(col[8]))

print(charge)
#f=open('charge.dat','w')
#f.write('{}'.format(charge))
#f.close()
