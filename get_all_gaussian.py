import glob
import numpy as np
import os


def getSubstringBetweenTwoChars(ch1,ch2,s):
    return s[s.find(ch1)+3:s.find(ch2)]


subdirs = [os.path.join('.', o) for o in os.listdir('.') if os.path.isdir(os.path.join('.',o))]
subdirs_mod = []
for i in subdirs:
    if i not in ('.','./optfile','./opt_mix','./.ipynb_checkpoints','./__pycache__','./log_rename','./original', './opt_xyz'):  #remove set of element
        subdirs_mod.append(i)
print(subdirs_mod)


start = 0
end = 0
begin = 0
last = 0

new = open("get_all_gaussian.csv","w")


for p in subdirs_mod:
    os.chdir(p)
    rline=open("save.log").readlines()
    if rline[-1][1:7] == 'Normal':
        file_read = open("save.log", "r")
        data = file_read.read()
        s2= getSubstringBetweenTwoChars('ntry.','\\@',data)
        string = s2
        new_string1 = string.replace("\n ", "")
        new_string2 = new_string1.replace("\\", "\n" ) 
        s = new_string2
        HF = getSubstringBetweenTwoChars('HF=', '\nS2',s)
        S2 = getSubstringBetweenTwoChars('S2=', '\nS2-1',s) 
        Dipole = getSubstringBetweenTwoChars('le=','\nQuadrupole', s)


         #get hirshfeld and CM5 charge of Fe
        for i in range(len(rline)):
            if "Hirshfeld charges, spin densities, dipoles, and CM5 charges using" in rline[i]:
                start = i
        for  m in range(start+2,len(rline)):
            if "with hydrogens summed into heavy atoms:" in rline[m]:
                end = m
                break

        for line in rline[start+2: end]:
            if "Fe" in line:
                fe_line = line.split()
                hirshfeld = fe_line[2]
                cm5 = fe_line[7]


        #get mulliken charge of Fe
        for l in range(len(rline)):
            if "Sum of Mulliken charge" in rline[l]:
                begin = l
        for k in range(begin+1,len(rline)):
            if "Electronic" in rline[k]:
                last = k
                break


        for line in rline[begin+2: last]:
            if "Fe" in line:
                fe_line = line.split()
                mulliken = fe_line[2]
    

    #get DDEC6

        all_xyz = glob.glob('*xyz')
        ok = "DDEC6_even_tempered_net_atomic_charges.xyz"
        if ok in all_xyz:
            f = open("DDEC6_even_tempered_net_atomic_charges.xyz", "r")
            r = f.read()
            para = getSubstringBetweenTwoChars('tensor','sperically',r)
            para1 = getSubstringBetweenTwoChars('Fe','sperically',para)
            DDEC6 = para1[40:50]


    #get bader charge
        com=np.loadtxt('../'+p[:-5]+'.xyz', skiprows=2, dtype=str)
        try: 
            dat=np.loadtxt('ACF.dat',skiprows=2, max_rows=len(com), dtype=str)
            everything=np.column_stack([com,dat])
            for col in everything:
                if col[0]=='Fe':
                    bader=float(8-float(col[8]))
        except FileNotFoundError:
            bader = 0.000000



        new.write('{}, {}, {}, {}, {}, {}, {}, {}, {}\n'.format(p[2:], HF, S2, Dipole, hirshfeld, cm5, mulliken, DDEC6, bader))
    os.chdir('../')

#wrise three charges in file    
new.close()

