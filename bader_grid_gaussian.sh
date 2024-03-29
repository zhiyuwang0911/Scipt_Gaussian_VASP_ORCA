#!/bin/bash
#SBATCH --job-name=bader.job
#SBATCH --output=bader.out
#SBATCH --error=bader.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=wangzhiyu@ufl.edu
#SBATCH --time=05:00:00
#SBATCH --mem=1gb
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1 # number of CPU core to use
#SBATCH --account=mingjieliu
#SBATCH --qos=mingjieliu

module load gaussian/16

formchk 2step.chk 2step.fchk
echo "-------------------------- processing grid 80 --------------------------"
cubegen 1 density=scf 2step.fchk 2step.cube 80 h
bader 2step.cube
cp ACF.dat ACF_80.dat

charge=`python /blue/mingjieliu/wangzhiyu/script/get_bader_single_gaussian.py`
echo "------------- charge at grid 80: $charge -------------"

nelec=`grep "NUMBER OF ELECTRONS" ACF.dat | awk '{print $4}'`
echo "------------- #electron at grid 80: $nelec -------------"

for i in {90..400..10}
do
echo "-------------------------- processing grid $i --------------------------"

cubegen 1 density=scf 2step.fchk 2step.cube $i h
bader 2step.cube
cp ACF.dat ACF_${i}.dat

charge2=`python /blue/mingjieliu/wangzhiyu/script/get_bader_single_gaussian.py`
echo "------------- charge at grid $i: $charge2 -------------"
diff=$(bc <<< "$charge - $charge2")
diff_abs=${diff#-}
echo "------------- charge difference: $diff_abs -------------"
charge=$charge2

nelec2=`grep "NUMBER OF ELECTRONS" ACF.dat | awk '{print $4}'`
echo "------------- #electron at grid $i: $nelec2 -------------"
diff_elec=$(bc <<< "$nelec - $nelec2")
diff_elec_abs=${diff_elec#-}
echo "------------- electron difference: $diff_elec_abs -------------"
nelec=$nelec2

if (( $(echo "$diff_abs < 0.02" |bc -l) )) && (( $(echo "$diff_elec_abs < 0.02" |bc -l) ))
then
  echo "############# final step: $i #############"
  echo "------------- final_charge_difference: $diff_abs -------------"
  echo "------------- final_electron_difference: $diff_elec_abs -------------"
  echo "------------- yay! converged!! -------------"
  break
fi
done
