# Passport Eye Demo
Demo project to test PassportEye python library


# conda related commads for this project

### create a new conda environment
conda create -n passporteyedemo
 
### activate environment
conda activate passporteyedemo

### export configuration to a file
conda env export > passporteyedemo.yml

### create a new conda environment from config file
conda env create  -f passporteyedemo.yml
