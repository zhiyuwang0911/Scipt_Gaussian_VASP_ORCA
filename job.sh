#!/bin/bash
#SBATCH --job-name=flake3.job
#SBATCH --output=flake3.out
#SBATCH --error=flake3.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=wangzhiyu@ufl.edu
#SBATCH --time=24:00:00
#SBATCH --mem=100gb
#SBATCH --nodes=1
#SBATCH --ntasks=16
#SBATCH --cpus-per-task=1 # number of CPU core to use
#SBATCH --account=mingjieliu
#SBATCH --qos=mingjieliu-b
module load gaussian
input=flake3.com
output=flake3_1_8.log
g16 < $input > $output
