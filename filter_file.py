#filter structure with the name list from other folder
import glob
import os
import shutil
import pandas as pd

new_folder = 'filter_281'
subfolder = 'final_filter_structure'
os.makedirs(new_folder, exist_ok=True)

all_xyz = glob.glob("*xyz")
print(all_xyz[-2:])
filter_xyz = glob.glob(subfolder+"/*.xyz")
print(filter_xyz[-2:])

filter_list=[]
for x in filter_xyz:
    filter_list.append(x[23:-10]+'_opt.xyz')
print(filter_list[-2:])
for i in all_xyz:
    if i in filter_list:
        print(i)
        shutil.copy(i, os.path.join(new_folder, i))
