import glob
import numpy as np
import os

subdirs = [os.path.join('.', o) for o in os.listdir('.') if os.path.isdir(os.path.join('.',o))]
subdirs_mod = []
for i in subdirs:
    if i not in ('.','./optfile','./opt_mix','./.ipynb_checkpoints','./opt','./log_rename','./original', './opt_xyz'):  #remove set of element
        subdirs_mod.append(i)
print(subdirs_mod)


start = 0
end = 0
begin = 0
last = 0

new = open("mulli_cm5_hirsh.csv","w")


for p in subdirs_mod:
    os.chdir(p)
    rline=open("2step.log").readlines()

    #get hirshfeld and CM5 charge of Fe
    for i in range(len(rline)):
        if "Hirshfeld charges, spin densities, dipoles, and CM5 charges using" in rline[i]:
            start = i
    for  m in range(start+2,len(rline)):
        if "with hydrogens summed into heavy atoms:" in rline[m]:
            end = m
            break
    print(start)
    print(end)


    for line in rline[start+2: end]:
        if "Fe" in line:
            fe_line = line.split()
            #print(fe_line)
            hirshfeld = fe_line[2]
            cm5 = fe_line[7]
            print(hirshfeld)
            print(cm5)

    
    #get mulliken charge of Fe
    for l in range(len(rline)):
        if "Sum of Mulliken charge" in rline[l]:
            begin = l
    for k in range(begin+1,len(rline)):
        if "Electronic" in rline[k]:
            last = k
            break

    print(begin)
    print(last)

    for line in rline[begin+2: last]:
        #print(line)
        if "Fe" in line:
            fe_line = line.split()
            #print(fe_line)
            mulliken = fe_line[2]
            print(mulliken)
    new.write('{}   {}   {}   {}\n'.format(p[2:], hirshfeld, cm5, mulliken))
    os.chdir('../')

#wrise three charges in file    
new.close()
 


    




    






