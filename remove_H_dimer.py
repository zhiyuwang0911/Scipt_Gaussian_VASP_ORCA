import os
import glob
import shutil

source_dir = './'
target_dir = './dimer_sub/'

os.makedirs(target_dir, exist_ok=True)
new_first_line = "25"

for files in os.listdir(source_dir):
    if files.endswith('.xyz'):
        print(files)
        source_file_path = os.path.join(source_dir, files)
        target_file_path = os.path.join(target_dir, files)

        with open(source_file_path, 'r') as file:
            lines = file.readlines()
        
        if lines:
            # Rewrite the first line
            lines[0] = new_first_line + '\n'
            # Remove the last line
            lines = lines[:-3] 
            lines[-1]=lines[-1]+'\n'

        # Write the modified content to a new file in the target directory
        with open(target_file_path, 'w') as file:
            file.writelines(lines)
