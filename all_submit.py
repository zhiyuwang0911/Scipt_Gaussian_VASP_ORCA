import numpy as np
import glob
import os
import shutil
import subprocess
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

    g_input.write('%chk=arm.chk\n')
    g_input.write('%mem=500gb\n')
    g_input.write('%NProcShared=32\n')
    g_input.write('%CPU=0-31\n')
    g_input.write('%GPUCPU=0-7=0-7\n')
    g_input.write('#n HF/3-21g Opt output=wfx scf=xqc pop=hirshfeld\n')
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
    g_input.write('{}.wfx'.format(system))
    g_input.close()
    
    #write job.sh file
    j_input=open('job.sh', 'w')
    j_input.write('#!/bin/bash\n')
    j_input.write('#SBATCH --job-name={}.job\n'.format(system))
    j_input.write('#SBATCH --mail-user=wangzhiyu@ufl.edu\n')
    j_input.write('#SBATCH --mail-type=FAIL,END\n')
    j_input.write('#SBATCH --error={}.err\n'.format(system))
    j_input.write('#SBATCH --cpus-per-task=1\n')
    j_input.write('#SBATCH --mem-per-cpu=15gb\n')
    j_input.write('#SBATCH --time=80:00:00\n')
    j_input.write('#SBATCH --distribution=cyclic:cyclic\n')
    j_input.write('#SBATCH --account=mingjieliu\n')
    j_input.write('#SBATCH --qos=mingjieliu\n')
    j_input.write('#SBATCH --ntasks=32\n')
    j_input.write('#SBATCH --partition=gpu\n')
    j_input.write('#SBATCH --gres=gpu:a100:8\n')
    j_input.write('module load gaussian/16-c02\n')
    j_input.write('input={}.com\n'.format(system))
    j_input.write('output={}.log\n'.format(system))
    j_input.write('g16 < $input > $output\n')
    j_input.close()
    #write 2step.com file
    step=open('2step.com', 'w')
    step.write('%OldChk=arm.chk\n')
    step.write('%Chk=2step.chk\n')
    step.write('%Mem=800gb\n')
    step.write('%NProcShared=32\n')
    step.write('%CPU=0-31\n')
    step.write('%GPUCPU=0-7=0-7\n')
    step.write('#n M06L/6-31G(d) Opt Geom=(AllCheck,Step=20) SCF=XQC Guess=Read Output=wfx Pop=Hirshfeld\n')
    step.write('\n')
    step.write('2step.wfx')
    step.close()
    #write 2step.sh submission file
    sub=open('2step.sh', 'w')
    sub.write('#!/bin/bash\n')
    sub.write('#SBATCH --job-name=2-{}.job\n'.format(system))
    sub.write('#SBATCH --mail-user=wangzhiyu@ufl.edu\n')
    sub.write('#SBATCH --mail-type=FAIL,END\n')
    sub.write('#SBATCH --error=2-{}.err\n'.format(system))
    sub.write('#SBATCH --cpus-per-task=1\n')
    sub.write('#SBATCH --mem-per-cpu=20gb\n')
    sub.write('#SBATCH --time=80:00:00\n')
    sub.write('#SBATCH --distribution=cyclic:cyclic\n')
    sub.write('#SBATCH --account=mingjieliu\n')
    sub.write('#SBATCH --qos=mingjieliu\n')
    sub.write('#SBATCH --ntasks=32\n')
    sub.write('#SBATCH --partition=gpu\n')
    sub.write('#SBATCH --gres=gpu:a100:8\n')
    sub.write('module load gaussian/16-c02\n')
    sub.write('input=2step.com\n'.format(system))
    sub.write('output=2step.log\n'.format(system))
    sub.write('g16 < $input > $output\n')
    sub.close()
    #write the job control file
    job_control=open('job_control.txt', 'w')
    job_control.write('<periodicity along A, B, and C vectors>\n')
    job_control.write('.false.\n')
    job_control.write('.false.\n')
    job_control.write('.false.\n')
    job_control.write('</periodicity along A, B, and C vectors>\n')
    job_control.write('\n')
    job_control.write('<atomic densities directory complete path>\n')
    job_control.write('/blue/mingjieliu/wangzhiyu/program/chargemol/chargemol_09_26_2017/atomic_densities/\n')
    job_control.write('</atomic densities directory complete path>\n')
    job_control.write('\n')
    job_control.write('<input filename>\n')
    job_control.write('2step.wfx\n')
    job_control.write('</input filename>\n')
    job_control.write('\n')
    job_control.write('<charge type>\n')
    job_control.write('DDEC6\n')
    job_control.write('</charge type>\n')
    job_control.close()
    
    subprocess.Popen('bash ../chain.sh',shell=True)
    os.chdir('../')
