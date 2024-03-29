import glob
import numpy as np
import os

def getSubstringBetweenTwoChars(ch1,ch2,s):
    return s[s.find(ch1)+6:s.find(ch2)-4]

subdirs = [os.path.join('.', o) for o in os.listdir('.') if os.path.isdir(os.path.join('.',o))]
subdirs_mod = []
for i in subdirs:
    if i not in ('.','./optfile','./opt_mix','./.ipynb_checkpoints','./opt','./log_rename','./original', './opt_xyz'):  #remove set of element
        subdirs_mod.append(i)
print(subdirs_mod)

new = open('DDEC6.csv','w')
for i in subdirs_mod:
    os.chdir(i)
    all_xyz = glob.glob('*xyz')
    ok = "DDEC6_even_tempered_net_atomic_charges.xyz"
    if ok in all_xyz:
        f = open("DDEC6_even_tempered_net_atomic_charges.xyz", "r")
        r = f.read()
        para = getSubstringBetweenTwoChars('tensor','sperically',r)
        #print(para)        
        #os.chdir('../')
        para1 = getSubstringBetweenTwoChars('Fe','sperically',para)
        #print(para1)
        DDEC6 = para1[40:50]
        print(DDEC6)
        new.write('{}     {}\n'.format(i, DDEC6))
        os.chdir('../')
new.close()
            
