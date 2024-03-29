import numpy as np
import glob
import os
import shutil
import subprocess


subdirs = [os.path.join('.', o) for o in os.listdir('.') if os.path.isdir(os.path.join('.',o))]
print(subdirs)
subdirs_mod=[]
for i in subdirs:
    #if i!='./.ipynb_checkpoints':   remove element
    if i not in ('./.ipynb_checkpoints','.'):  #remove set of element
        subdirs_mod.append(i)
print(subdirs_mod)

for i in subdirs_mod:
    os.chdir(i)
    try:
        all_log = glob.glob('*.log')
        #for j in all_log:
            #if '2step.log' not in j:

        suchas = "2step.log"
        if suchas in all_log:
            all_log.remove(suchas)
        for j in all_log:
            read_log = open(j).readlines()
            if read_log[-5][1:8] == 'Density':
            elif read_log[-5][1:12] == 'Convergence':
            elif read_log[0][:6] == 'ntrbks':
            elif read_log[0][1:7] == 'LinEq1':
            elif read_log[1][4:11] == 'special'
            elif read_log[0][4:11] == 'special' 
                all_com = glob.glob('*.com')
                for a in all_com:
                    if '2step.com' not in a:
                        read_com = open(a).readline()
                        read_com[3] = '#n HF/3-21g Opt output=wfx scf=(NoVarAcc,NoIncFock,Fermi,XQC)  NoSymm  pop=hirshfeld'
                        print(read_com[3])
                        f = open(a,'w')
                        for line in read_com:
                            a.write(line)
                            a.close()
                    elif '2step.com' in a:
                        read_com = open(a).readline()
                        read_com[4] = '#n M06L/6-31g(d) Opt Geom=(AllCheck,Step=20) Guess=read output=wfx SCF=(NoVarAcc,NoIncFock,Fermi,XQC)  NoSymm  pop=hirshfeld'
                        print(read_com[3])
                        f = open(a,'w')
                        for line in read_com:
                            a.write(line)
                            a.close()
                            #subprocess.Popen('bash /blue/mingjieliu/wangzhiyu/flake_spin/chain_1step.sh',shell=True)
            #elif read_log[-1][1:6] == 'ntrbk':
                #all_com = glob.glob('*.com')
                #for a in all_com:
                    #if '2step.com' not in a:
                    #read_com = open(a).readline()
                    #read_com[3] = '................'
                    #f = open(a,'w')
                    #for line in read_com:
                        #a.write(line)
                        #a.close()
                        #subprocess.Popen('bash /blue/mingjieliu/wangzhiyu/flake_spin/chain_1step.sh',shell=True)


            elif:
                pass

        #elif for p in all_log:
         #   if '2step.log' not in p:
          #      read = open(j),readline()
            #elif read_log[-1][1:7] == 'Normal'
                #read_agin = open('2step.log').readline()
                #read_com = open('2step.com').readline()
                #if read_agin[-5][1:12] == 'Convergence':
                    #read_com[3] = '................'
                    #f = open('2step.com','w')    #rewrite 2step.log file
                    #for line in read_com:
                        #f.write(line)
                        #f.close()
                        #subprocess.Popen('bash /blue/mingjieliu/wangzhiyu/flake_spin/chain_2step.sh',shell=True)
                #elif read_again[-1][1:6] == 'ntrbk'
                    #read_com[3] = '................'
                    #f = open('2step.com','w')
                    #for line in read_com:
                        #f.write(line)
                        #f.close()
                        #subprocess.Popen('bash /blue/mingjieliu/wangzhiyu/flake_spin/chain_2step.sh',shell=True)
                #elif:
                    #pass

    except:
        pass
