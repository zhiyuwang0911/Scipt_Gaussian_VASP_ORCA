import glob
import numpy as np
import os


def getSubstringBetweenTwoChars(ch1,ch2,s):
    return s[s.find(ch1)+3:s.find(ch2)]


subdirs = [os.path.join('.', o) for o in os.listdir('.') if os.path.isdir(os.path.join('.',o))]
subdirs_mod = []
for i in subdirs:
    if i not in ('.','./opt_mix','./.ipynb_checkpoints','./__pycache__', './opt_xyz'):  #remove set of element
        subdirs_mod.append(i)
print(subdirs_mod)


start = 0
end = 0
begin = 0
last = 0


new = open("prop-BLYP-int.csv","w")


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
        if "UBLYP" in s: 
            HF = getSubstringBetweenTwoChars('HF=', '\nS2',s)   # change to string later and convert to eV
        #S2 = getSubstringBetweenTwoChars('S2=', '\nS2-1',s)
        else:
            HF = getSubstringBetweenTwoChars('HF=', '\nRMSD',s)
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
                #print(mulliken)
        
        
        #get H-L gap
        for  h in  rline:
            if "Alpha  occ. eigenvalues" in h:
                h_line = h.split()
                HOMO = h_line[-1]
            
            if "Alpha virt. eigenvalues" in h:
                l_line = h.split()
                print(l_line)
                LUMO = l_line[4]
                #print(lines)
                #HUMO = lines[4]
                print(LUMO)
                break

        new.write('{}, {}, {}, {}, {}, {}, {}, {}\n'.format(p[2:], HF, HOMO, LUMO, hirshfeld, cm5, mulliken, Dipole)) 
    os.chdir('../')


new.close()




