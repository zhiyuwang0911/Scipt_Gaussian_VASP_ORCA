import glob
import os
import numpy as np
import subprocess

subdirs = [os.path.join('.', o) for o in os.listdir('.') if os.path.isdir(os.path.join('.',o))]
subdirs_mod=[]
for i in subdirs:
    if i not in ('.', './opt_xyz'):  #remove set of element
        subdirs_mod.append(i)

for j in subdirs_mod:
    os.chdir(j)
    log = glob.glob('save.log')
    if len(log)== 0:
        subprocess.Popen('sbatch job.sh',shell=True)
    os.chdir('../')
