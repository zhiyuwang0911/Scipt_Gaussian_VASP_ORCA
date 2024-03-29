import numpy as np
import glob
import os
import shutil
import subprocess

subdirs = [os.path.join('.', o) for o in os.listdir('.') if os.path.isdir(os.path.join('.',o))]
print(subdirs)
for x in subdirs:
    os.chdir(x)
    print(x)
    subprocess.Popen('sbatch job.sh',shell=True)
    os.chdir('../')
