import numpy as np
import glob
import os


def getSubstringBetweenTwoChars(ch1,ch2,inpt_str):
    return s[s.find(ch1)+4:s.find(ch2)] 

current = os.getcwd()
subfolders = glob.glob('*/')

print(subfolders)

for name in subfolders:
    os.chdir(name)
    log = glob.glob('save.log')
    if len(log) == 0:
        print(name)
        subfolders.remove(name)
    os.chdir(current)

print(subfolders)


try:
    os.mkdir('opt_xyz/')
except:
    pass
dest='../opt_xyz/'



for i in subfolders:
    os.chdir(i)
    print(os.getcwd())


    file = open("save.log", "r")
    s = file.read()

    s2= getSubstringBetweenTwoChars('entry.','\\@',s)

    new_string1 = s2.replace("\n ", "")
    new_string2 = new_string1.replace("\\", "\n" )
    new_string3 = new_string2.replace("0,2", "xxx" )
    new_string4 = new_string3.replace("0,1", "xxx" )
    new_string5 = new_string4.replace("Version","yyy")
    s = new_string5.replace(",","     ")

    s3= getSubstringBetweenTwoChars('xxx','yyy',s)
    s4=s3.splitlines()
    to=len(s4)-1
    total=str(to)
    str3 = "{}\n\n {}\n".format(total, s3)
    newfile=str(i[0:len(i)-1]) + "_opt.xyz"
    print(newfile)
    xyz = open(dest+newfile, 'w')
    xyz.write(str3)
    xyz.close()
    
    os.chdir('../')

