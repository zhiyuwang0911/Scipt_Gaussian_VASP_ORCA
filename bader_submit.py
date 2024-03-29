import os
import shutil
import subprocess

subdirs = [os.path.join('.', o) for o in os.listdir('.') if os.path.isdir(os.path.join('.',o))]
#print(subdirs)
subdirs_mod=[]
for i in subdirs:
    if i not in ('.','./.ipynb_checkpoints','./opt','./log_rename','./original', './opt_xyz'):  #remove set of element
        subdirs_mod.append(i)
print(subdirs_mod)
#print(sub_string)
for x in subdirs_mod:
    os.chdir(x)
    subprocess.Popen('sbatch ../bader_charge.sh',shell=True)
    os.chdir('../')
