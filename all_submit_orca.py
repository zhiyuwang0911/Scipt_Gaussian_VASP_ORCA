import numpy as np
import glob
import os
import shutil
import subprocess
namelist={'H': 1,'Cu':29,'C':6,'B':5,'N': 7,'O':8,'Fe':26,'S':16,'P':15}
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
    
    #write .inp file
    g_input=open('{}.inp'.format(system),'w')
    if odd_even==0:
        g_input.write('!DLPNO-CCSD(T) Extrapolate(3/4,def2) def2-QZVPP/C TIGHTSCF  hirshfeld\n')
    else:
        g_input.write('!DLPNO-CCSD(T) Extrapolate(3/4,def2) def2-QZVPP/C UNO TIGHTSCF  hirshfeld\n')
    g_input.write('%maxcore 15000\n')
    g_input.write('%pal\n')
    g_input.write('nprocs 6 \n')
    g_input.write('end\n')
    g_input.write('end\n')
    g_input.write('%mdci\n')
    g_input.write('maxiter 500\n')
    g_input.write('end\n')
    if odd_even==0:
        g_input.write('* xyz 0 1\n')
    else:
        g_input.write('* xyz 0 2\n')
    for i in atom_with_coordinate:
        g_input.write(i)
    g_input.write('*\n')
    g_input.close()
    
    #write job.sh file
    j_input=open('job.sh', 'w')
    j_input.write('#!/bin/bash\n')
    j_input.write('#SBATCH --job-name={}.job\n'.format(system))
    j_input.write('#SBATCH --mail-user=wangzhiyu@ufl.edu\n')
    j_input.write('#SBATCH --mail-type=FAIL,END\n')
    j_input.write('#SBATCH --error={}.err\n'.format(system))
    j_input.write('#SBATCH --cpus-per-task=1\n')
    j_input.write('#SBATCH --mem=95gb\n')
    j_input.write('#SBATCH --time=20:00:00\n')
    j_input.write('#SBATCH --nodes=1\n')
    j_input.write('#SBATCH --account=mingjieliu\n')
    j_input.write('#SBATCH --qos=mingjieliu-b\n')
    j_input.write('#SBATCH --ntasks=6\n')
    j_input.write('module load intel/2020.0.166 openmpi/4.1.5\n')
    j_input.write('/blue/mingjieliu/wangzhiyu/program/orca/orca {}.inp. > {}.out\n'.format(system,system))
    j_input.close()
    
    
    #subprocess.Popen('sbatch job.sh',shell=True)
    os.chdir('../')
