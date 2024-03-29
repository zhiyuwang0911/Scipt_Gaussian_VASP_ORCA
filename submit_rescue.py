import numpy as np
import glob
import os
import shutil
import subprocess


subdirs = [os.path.join('.', o) for o in os.listdir('.') if os.path.isdir(os.path.join('.',o))]
subdirs_mod=[]
for i in subdirs:
    #if i!='./.ipynb_checkpoints':   remove element
    if i not in ('./.ipynb_checkpoints','.'):  #remove set of element
        subdirs_mod.append(i)

for i in subdirs_mod:
    #print(i)
    os.chdir(i)
    try:
        log = glob.glob('*.log')
        suchas = "save.log"
        if suchas in log:
            read_log = open(suchas).readlines()
            #print(read_log[-5])
            #print(read_log[-5][1:12])
            #print(i)
            if read_log[-5][1:12] == 'Convergence':
                print(i)
            #elif read_log[-5][1:8] == 'Density':
            #elif read_log[0][:6] == 'ntrbks':
            #elif read_log[0][1:7] == 'LinEq1':
            #elif read_log[1][4:11] == 'special'
            #elif read_log[0][4:11] == 'special' 
                all_com = glob.glob('*.com')
                for a in all_com:
                    read_com = open(a).readlines()
                    #print(read_com[2])
                    read_com[2] = '#n M11 /6-311+g** scf=(NoVarAcc,NoIncFock,XQC,IntRep)  pop=hirshfeld\n'

                    print(read_com[2])

                    #print(read_com)
                    #print(a)
                    f = open(a,'w')
                    for line in read_com:
                        f.write(line)
                    f.close()
                    subprocess.Popen('sbatch job.sh',shell=True)

            else:
                pass
    
    except:
        pass
    os.chdir('../')
