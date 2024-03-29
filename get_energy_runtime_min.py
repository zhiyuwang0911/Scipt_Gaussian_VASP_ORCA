import os
import glob

def getSubstringBetweenTwoChars(ch1,ch2,s):
    return s[s.find(ch1)+3:s.find(ch2)]

subdirs = [os.path.join('.', o) for o in os.listdir('.') if os.path.isdir(os.path.join('.',o))]
print(subdirs)
subdirs_mod=[]
for i in subdirs:
    #if i!='./.ipynb_checkpoints':   remove element
    if i not in ('./.ipynb_checkpoints','.'):  #remove set of element
        subdirs_mod.append(i)
#print(i)

new = open("energy_runtime_FeN4_6-31g.csv","w")

for folder in subdirs_mod:
    os.chdir(folder)
    rline=open("save.log").readlines()
    if rline[-1][1:7] == 'Normal':
        #print(folder)
        line = rline[-4]
        split_line = line.split()
        time = round((float(split_line[-6]) + float(split_line[-4]) / 60 + float(split_line[-2]) / 360), 1)
        #time = round(float(split_line[-6])+float(split_line[-4]/60)+float(split_line[-2])/360),1)
        print(time)
        file_read = open("save.log", "r")
        data = file_read.read()
        s2= getSubstringBetweenTwoChars('ntry.','\\@',data)
        string = s2
        new_string1 = string.replace("\n ", "")
        new_string2 = new_string1.replace("\\", "\n" )
        s = new_string2
        if "UPBE1PBE" in s:
            HF = getSubstringBetweenTwoChars('HF=', '\nS2',s)   # change to string later and convert to eV
        else:
            HF = getSubstringBetweenTwoChars('HF=', '\nRMSD',s)
        energy  = round(float(HF)*27.21,4)
        print(energy)
    else:
        energy = 0.0000
        time = 000000
        print(time)
        print(energy)
    
    new.write('{}, {}, {}\n'.format(folder[2:],  energy,  time))
    os.chdir('../')


new.close()
