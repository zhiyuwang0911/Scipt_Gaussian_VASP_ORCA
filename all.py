import numpy as np
import glob
import os
import shutil
namelist={'H': 1,'C':6,'B':5,'N': 7,'O':8,'Fe':26}
all_xyz=glob.glob('*xyz')

print(os.getcwd())
for x in all_xyz:
    system=x[:-4]
    #os.mkdir(system)
    os.chdir(system)
    xyz=open('../{}.xyz'.format(system)).readlines()
    atom_with_coordinate=xyz[2:]
    atoms=np.loadtxt('../{}.xyz'.format(system),skiprows=2, dtype=str)[:,0]
    count=0
    for i in atoms:
        count+=namelist[i]
    odd_even=count%2
    
    #write .com file
    g_input=open('{}.com'.format(system),'w')

    g_input.write('%chk={}.chk\n'.format(system))
    g_input.write('%mem=400mW\n')
    g_input.write('%NProcShared=32\n')
    g_input.write('%CPU=0-31\n')
    g_input.write('%GPUCPU=0-5=0-1,16-19\n')
    g_input.write('#n M06L/6-31G(d) Opt output=wfx scf=xqc pop=hirshfeld\n')
    g_input.write('\n')
    g_input.write(' {}\n'.format(system))
    g_input.write('\n')
    if odd_even==0:
        g_input.write('0 1\n')
    else:
        g_input.write('0 2\n')
    for i in atom_with_coordinate:
        g_input.write(i)
    g_input.write('\n')
    g_input.write('{}wfx'.format(system))
    g_input.close()
    
    #write job.sh file
    
    os.chdir('../')

