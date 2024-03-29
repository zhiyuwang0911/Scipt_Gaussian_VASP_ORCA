#!/bin/bash
#SBATCH --job-name=bader.job
#SBATCH --output=bader.out
#SBATCH --error=bader.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=wangzhiyu@ufl.edu
#SBATCH --time=00:10:00
#SBATCH --mem=1gb
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1 # number of CPU core to use
#SBATCH --account=mingjieliu
#SBATCH --qos=mingjieliu-b

module load gaussian/16
formchk 2step.chk 2step.fchk
cubegen 1 density=scf arm.fchk 2step.cube 80 h
bader 2step.cube
