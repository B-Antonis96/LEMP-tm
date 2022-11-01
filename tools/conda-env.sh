#!/bin/sh

PROJECT_NAME="lemp-tm"
PYTHON_VERSION="3.10"

echo "Setting up conda environment for $PROJECT_NAME (python $PYTHON_VERSION)"

if command -v conda
then
    conda create --name $PROJECT_NAME python=$PYTHON_VERSION -y
    exit 0
else
    echo "Conda is not installed!"
    exit 1
fi
