import os 
import glob

all_xyz=glob.glob('*xyz')
print(all_xyz)
try:
    os.mkdir('xyz_bsse')
except:
    pass

for i in all_xyz:
    xyz_open = open(i,'r')
    xyz_lines = xyz_open.readlines()
    #print(xyz_lines)


    new_xyz = open('xyz_bsse/'+i[:-7]+'bsse.xyz', 'w')
    
    for j,line in enumerate(xyz_lines):
        #print(line)
        line_split = line.split(' ')
        #print(line_split)
        if j > 2 and j < 27:
            line_split[0] = line_split[0]+'(Fragment=1)'
        elif j == 27:
            line_split[0] = line_split[0]+'(Fragment=2)'
        elif j ==2:
            line_split[1] = line_split[1]+'(Fragment=1)'
        #print(line_split)
        new_string = " ".join(line_split)
        print(new_string)
        new_xyz.write('{}'.format(new_string))
    new_xyz.close()



        

        
