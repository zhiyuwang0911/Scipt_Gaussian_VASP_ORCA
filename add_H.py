import glob



all_xyz = glob.glob('*xyz')

for j in all_xyz:
    print(j)
    f_read =open(j).readlines()
    total_atom =int(f_read[0])
    print(total_atom)

    f=open(j[:-4]+'-H.xyz',"w")
    f.write('{}\n'.format(total_atom+1))
    for i in f_read[1:-1]:
        #print(i)
        new_line = i.split()

    #print(new_line)
        if new_line[0] == 'Fe':
            x1 = float(new_line[1])
            y1 = float(new_line[2])
            z1 = float(new_line[3])
            #print(x1,y1,z1)
    
            #f_read.write('C  {}  {}\n'.format(x1,y1,z1+2))
            #f_read.write('O  {}  {}\n'.format(x1,y1,z1+3.128))
        f.write(i)
    f.write('H  {}  {}   {}\n'.format(x1,y1,z1+1.700))
    f.close()        



