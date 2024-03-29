import os
import shutil
try:
    os.mkdir('/blue/mingjieliu/wangzhiyu/optfile')
except:
    pass
dest='/blue/mingjieliu/wangzhiyu/optfile/'
#subdirs = [x[0] for x in os.walk('.')]
subdirs = [os.path.join('.', o) for o in os.listdir('.') if os.path.isdir(os.path.join('.',o))]
print(subdirs)
subdirs_mod=[]
for i in subdirs:
    #if i!='./.ipynb_checkpoints':   remove element
    if i not in ('./.ipynb_checkpoints','.','./optfile'):  #remove set of element
        subdirs_mod.append(i)
print(subdirs_mod)
for i in subdirs_mod:
    try:
        read_log=open(i+"/2step.log").readlines()
        if read_log[-1][1:7] == 'Normal':
            shutil.copytree(i,dest+i)
            print(i)
    except:
        pass
