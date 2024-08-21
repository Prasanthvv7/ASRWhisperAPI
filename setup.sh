#!/bin/bash

# Update system package index
sudo apt-get update

# Install necessary system dependencies
sudo apt-get install -y ffmpeg

# Create a Python virtual environment
python3 -m venv venv

# Activate the virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install the required Python packages
pip install flask transformers torch librosa


echo "Setup completed successfully."
