#!/bin/bash

# Update the package lists and install updates
echo "Updating package lists and installing updates..."
sudo apt update
sudo apt upgrade -y

# Install Python 3, pip, virtualenv, and Git
echo "Installing Python 3, pip, virtualenv, and Git..."
sudo apt install -y python3-pip python3-venv git

# Clone the repository
echo "Cloning the repository..."
git clone -b Deployment https://github.com/Harshithvarma007/LLM_Text_Detection.git
cd LLM_Text_Detection

# Set up virtual environment
echo "Setting up virtual environment..."
python3 -m venv venv
source venv/bin/activate

# Install Python dependencies
echo "Installing Python dependencies..."
pip install -r requirements.txt

# Run the Streamlit app as a background service
echo "Running the Streamlit app as a background service..."
nohup streamlit run app.py --server.port 8501 > streamlit.log 2>&1 &

echo "Streamlit app is now running in the background."
echo "You can access it at http://localhost:8501"

# Optionally, you can add more instructions or cleanup steps here
