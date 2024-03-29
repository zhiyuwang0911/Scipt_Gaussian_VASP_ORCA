import glob
import os
import numpy as np

f = open('ACF.dat').readlines()[-5].strip('\n').split()[4]

print(f)
