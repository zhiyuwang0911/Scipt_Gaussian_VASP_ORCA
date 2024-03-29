import os
import shutil
import glob

source_folder = "./"
destination_folder = "../armchair-2-p5/"


start_index = 2001
end_index = 2551  # Adjust the end index as needed

files_in_source = os.listdir(source_folder)

# Ensure destination folder exists, create if it doesn't
os.makedirs('../armchair-2-p5/', exist_ok=True)

# Copy files at the specified indices
for index in range(start_index, end_index):
    if 0 <= index < len(files_in_source):
        file_to_copy = files_in_source[index]
        source_path = os.path.join(source_folder, file_to_copy)
        destination_path = os.path.join(destination_folder, file_to_copy)
        
        # Copy the file to the destination folder
        shutil.copy2(source_path, destination_path)
        print(f"Copied: {file_to_copy}")
    else:
        print(f"Index {index} is out of range")

print("Copy completed.")
