#!/bin/bash
#SBATCH --job-name=jnb
#SBATCH --output=jupyter.out
#SBATCH --error=jupyter.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=wangzhiyu@ufl.edu
#SBATCH --time=10:00:00
#SBATCH --mem=40gb
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1 # number of CPU core to use
#SBATCH --account=mingjieliu
#SBATCH --qos=mingjieliu
pwd; hostname; date
jupyter notebook --ip $(hostname) --no-browser
