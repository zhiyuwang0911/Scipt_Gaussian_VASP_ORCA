#!/bin/bash
#SBATCH --job-name=bader.job
#SBATCH --output=bader.out
#SBATCH --error=bader.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=wangzhiyu@ufl.edu
#SBATCH --time=50:00:00
#SBATCH --mem=25gb
#SBATCH --nodes=2
#SBATCH --ntasks=32
#SBATCH --cpus-per-task=1 # number of CPU core to use
#SBATCH --account=mingjieliu
#SBATCH --qos=mingjieliu
#SBATCH --distribution=cyclic:cyclic

module purge
module load intel/2018 openmpi/3.0.0 vasp/5.4.4

a=200
b=200
c=50
iterations=20

cat <<EOF>INCAR
NSW = 0
Prec = Accurate
LAECHG = TRUE
LCHARG = TRUE
ENCUT = 500.00 eV
METAGGA = M06L
NGXF = 200
NGYF = 200
NGZF = 40
EOF
srun  vasp_std
chgsum.pl AECCAR0 AECCAR2
bader CHGCAR -ref CHGCAR_sum
cp ACF.dat ACF_1.dat

charge=`python /blue/mingjieliu/wangzhiyu/revision/vasp/FeO_M06L_B/get_bader_single_vasp.py`
echo "------------- charge at grid 1 round: $charge -------------" 


nelec=`grep "NUMBER OF ELECTRONS" ACF.dat | awk '{print $4}'`
echo "------------- #electron at grid 1 round: $nelec -------------"
 

for ((i=0; i<iterations; i++)) 
do
# Perform operations with a, b, and c (replace this line with your desired logic)
# Increment the variables
a=$((a + 50))
b=$((b + 50))
c=$((c + 20))
echo "Values: a=$a, b=$b, c=$c"

cat <<EFO>INCAR
NSW = 0
Prec = Accurate
LAECHG = TRUE
LCHARG = TRUE
ENCUT = 500.00 eV
METAGGA = M06L
NGXF = $a
NGYF = $b
NGZF = $c
EFO
srun  vasp_std
chgsum.pl AECCAR0 AECCAR2
bader CHGCAR -ref CHGCAR_sum
cp ACF.dat ACF_${a}.dat

charge2=`python /blue/mingjieliu/wangzhiyu/revision/vasp/FeO_M06L_B/get_bader_single_vasp.py`
echo "------------- charge at grid $a: $charge2 -------------"
diff=$(bc <<< "$charge - $charge2")
diff_abs=${diff#-}
echo "------------- charge difference: $diff_abs -------------"
charge=$charge2

nelec2=`grep "NUMBER OF ELECTRONS" ACF.dat | awk '{print $4}'`
echo "------------- #electron at grid $a: $nelec2 -------------"
diff_elec=$(bc <<< "$nelec - $nelec2")
diff_elec_abs=${diff_elec#-}
echo "------------- electron difference: $diff_elec_abs -------------"
nelec=$nelec2

if (( $(echo "$diff_abs < 0.02" |bc -l) )) && (( $(echo "$diff_elec_abs < 0.02" |bc -l) ))
then
  echo "############# final step: $a #############"
  echo "------------- final_charge_difference: $diff_abs -------------"
  echo "------------- final_electron_difference: $diff_elec_abs -------------"
  echo "------------- yay! converged!! -------------"
  break
fi
done
