#!/bin/bash
#SBATCH --job-name=charge.job
#SBATCH --output=ar4fc3_1_0_wfx.out
#SBATCH --error=ar4fc3_1_0_wfx.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=wangzhiyu@ufl.edu
#SBATCH --time=1:00:00
#SBATCH --mem=1gb
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1 # number of CPU core to use
#SBATCH --account=mingjieliu
#SBATCH --qos=mingjieliu-b
Chargemol_09_26_2017_linux_serial
