import os
import glob
import numpy as np
import ase
from ase import io

#put script one layer up than xyz file
#read original and relaxed xyz file
xyz1 = glob.glob('opt/*.xyz')
xyz2 = glob.glob('original/*.xyz')

#get absolute z value change of Fe atom
loc = open('local_curvature.dat', 'w')  
xyz1.sort()
xyz2.sort()
for i in range(len(xyz1)):
    f=io.read(xyz1[i])
    opt=f.arrays['positions'][list(f.arrays['numbers']).index(26)][2]
    g=io.read(xyz2[i])
    org=g.arrays['positions'][list(g.arrays['numbers']).index(26)][2]
    sub=opt-org
    loc.write('{}    {:.10f}\n'.format(xyz1[i][4:12], abs(sub)))
loc.close()
