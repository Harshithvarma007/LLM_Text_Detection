#!/bin/bash

# Update and install dependencies
sudo apt update
sudo apt upgrade -y
sudo apt install -y python3-pip python3-venv git

# Clone the repository
git clone -b Deployment https://github.com/Harshithvarma007/LLM_Text_Detection.git
cd LLM_Text_Detection

# Set up virtual environment and install Python dependencies
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Configure Streamlit to run on port 80
mkdir -p ~/.streamlit
echo "[server]
headless = true
enableCORS = false
port = 80" > ~/.streamlit/config.toml

# Run the Streamlit app
nohup streamlit run app.py &
