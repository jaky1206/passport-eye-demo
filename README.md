# Passport Eye Demo

## Overview
This repository contains a demo project to test the PassportEye python library and Tesseract OCR.

## Conda Environment Setup

### Create a new conda environment
```shell
conda create -n passporteyedemo
```

### Activate the environment
```shell
conda activate passporteyedemo
```

### Export configuration to a file
```shell
conda env export > passporteyedemo.yml
```

### Create a new conda environment from the config file
```shell
conda env create -f passporteyedemo.yml
```

## Conda Environment Setup
Repository Structure
- .gitignore: Contains files and directories to be ignored by git.
- README.md: Provides information about the project and setup instructions.
- main.py: The main Python script for the demo.

## Languages
- Python

## Acknowledgments
- https://ourcodeworld.com/articles/read/656/how-to-retrieve-machine-readable-zones-from-a-passport-image-with-python-using-the-passporteye-library
