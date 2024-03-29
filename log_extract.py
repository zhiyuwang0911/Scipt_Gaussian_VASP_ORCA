import os
import shutil 
subdirs = [os.path.join('.', o) for o in os.listdir('.') if os.path.isdir(os.path.join('.',o))]
print(subdirs)
os.mkdir('log_rename')
for i in subdirs:
    #system=i
    os.chdir(i)
    try:

        #os.rename('2step.log','{}_final.log'.format(i))
        origin = './'
        target = '../log_rename/'
        shutil.copy(origin + '2step.log', target +'{}.log'.format(i))
        print("Files are copied successfully")
    except:
        print('not a correct directory')
        pass
    os.chdir('../')
    

