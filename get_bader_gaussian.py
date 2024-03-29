import glob
import os
import numpy as np
subdirs = [os.path.join('.', o) for o in os.listdir('.') if os.path.isdir(os.path.join('.',o))]
subdirs_mod=[]
for i in subdirs:
    if i not in ('.','./opt_mix','./optfile','./.ipynb_checkpoints','./opt','./log_rename','./original', './opt_xyz'):  #remove set of element
        subdirs_mod.append(i)

new=open('bader.csv','w')
for i in subdirs_mod:
    os.chdir(i)
    xyz=np.loadtxt(i+'_opt.xyz', skiprows=2, dtype=str)
    dat=np.loadtxt('ACF.dat',skiprows=2, max_rows=len(xyz), dtype=str)
    everything=np.column_stack([xyz,dat])
    for col in everything:
        if col[0]=='Fe':
            charge=float(8-float(col[8]))
    new.write('{} ,{}\n'.format(i, charge))
    os.chdir('../')
new.close()
