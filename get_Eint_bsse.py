import glob
import numpy as np
import os


#def getSubstringBetweenTwoChars(ch1,ch2,s):
#    return s[s.find(ch1)+3:s.find(ch2)]


subdirs = [os.path.join('.', o) for o in os.listdir('.') if os.path.isdir(os.path.join('.',o))]
subdirs_mod = []
for i in subdirs:
    if i not in ('./.ipynb_checkpoints','./__pycache__','./log_rename','./opt_xyz'):  #remove set of element
        subdirs_mod.append(i)
print(subdirs_mod)

start = 0
end = 0

with open("BSSE-low.csv", "w") as afile:
    for files in sorted(subdirs_mod):
        os.chdir(files)
        rline = open("save.log", "r").readlines()

        for i in range(len(rline)):
            if "complexation energy =" in rline[i]:
                start = i
        for m in range(start,len(rline)):
            if "Unable to Open any file for archive entry" in rline[m]:
                end = m
                break

        for line in rline[start: end]:
            if "corrected" in line:
                that_line = line.split()
                Eint = float(that_line[3])*0.04336
                print(Eint)

        afile.write(f"{files[2:9]}, {Eint}\n")
        os.chdir('../')
