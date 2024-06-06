#!/bin/bash

# If virtualenv is not installed install it
if ! command -v virtualenv &> /dev/null; then
    echo "virtualenv not found. Installing..."
    pip install virtualenv
fi

# Create the virtual environment
virtualenv spatialVEnv

# Activate / Go into virtual environment
source spatialVEnv/bin/activate

# install the notebook in the virtual environment
pip install jupyter

# Install the packages reading them line by line from the requirements file
pip install -r requirements.txt 


# Exit the virtual environment (in the command line that is)
deactivate
