#!/bin/bash

script=job.sh

PID=$(sbatch $script|awk '{print $NF}')
echo $PID

script=2step.sh

PID_2=$(sbatch --dependency=afterany:$PID $script|awk '{print $NF}')
echo $PID_2

script=../j1.sh

PID_3=$(sbatch --dependency=afterany:$PID_2  $script| awk '{print $NF}')
echo $PID_3

script=../bader_charge.sh

PID_4=$(sbatch --dependency=afterany:$PID_3  $script| awk '{print $NF}')
echo $PID_4

