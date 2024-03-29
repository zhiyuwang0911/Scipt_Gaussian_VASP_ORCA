#!/bin/bash

# Assigning values to variables
xyz_dir="./"
amplitude="0.1"

# Loop through each XYZ file in the directory
for file in "${xyz_dir}"/*.xyz; do
    # Check if the file is a regular file
    if [ -f "$file" ]; then
        # Run the conversion scripts
        xyz2poscar.py "$file" "${file%.xyz}_poscar"
        poscar2acf.py "${file%.xyz}_poscar" > "${file%.xyz}.acf"
        acf_shake.py "${file%.xyz}.acf" "$amplitude" > "${file%.xyz}_${amplitude}.acf"
        acf2xyz.py "${file%.xyz}_${amplitude}.acf" > "${file%.xyz}_${amplitude}.xyz"
    fi
done

echo "Done!"
