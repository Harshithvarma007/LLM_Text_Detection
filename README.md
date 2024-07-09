To deploy your Streamlit app on an AWS Ubuntu instance using the provided GitHub repository, follow these steps:

### Step 1: Set Up an AWS EC2 Instance
1. **Launch an AWS EC2 Instance**:
    - Go to the [AWS Management Console](https://aws.amazon.com/console/).
    - Launch a new EC2 instance.
    - Select an Ubuntu Server 20.04 LTS (or newer) Amazon Machine Image (AMI).
    - Choose an instance type (t2.micro should be sufficient for testing purposes).
    - Configure security groups to allow HTTP (port 80) and SSH (port 22) access.

2. **Connect to Your Instance**:
    - Use SSH to connect to your instance:
      ```sh
      ssh -i /path/to/your-key-pair.pem ubuntu@your-instance-public-dns
      ```

### Step 2: Install Required Software on Your Instance
1. **Update Package Lists and Install Dependencies**:
    ```sh
    sudo apt update
    sudo apt upgrade -y
    sudo apt install -y python3-pip python3-venv git
    ```

2. **Install and Configure Docker (Optional)**:
    If you prefer to use Docker for deployment, install Docker:
    ```sh
    sudo apt install -y docker.io
    sudo usermod -aG docker ubuntu
    newgrp docker
    ```

### Step 3: Clone Your GitHub Repository
1. **Clone the Repository**:
    ```sh
    git clone -b Deployment https://github.com/Harshithvarma007/LLM_Text_Detection.git
    cd LLM_Text_Detection
    ```

### Step 4: Set Up and Run the Streamlit App
1. **Create a Virtual Environment and Install Dependencies**:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

2. **Run the Streamlit App**:
    ```sh
    streamlit run app.py
    ```

### Step 5: Configure the App to Run on AWS
1. **Edit the Streamlit Configuration**:
    Open or create the `.streamlit/config.toml` file in your project directory and add the following lines to set the app to run on the public DNS and port 80:
    ```toml
    [server]
    headless = true
    enableCORS = false
    port = 80
    ```

2. **Run the Streamlit App as a Background Service**:
    ```sh
    nohup streamlit run app.py &
    ```

### Step 6: Access Your Streamlit App
- Open a web browser and navigate to `http://your-instance-public-dns`.

### Full Script for Automation
You can create a shell script to automate these steps:

```sh
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
```

### Running the Automation Script
- Save the script above as `deploy.sh`.
- Make it executable:
  ```sh
  chmod +x deploy.sh
  ```
- Run the script:
  ```sh
  ./deploy.sh
  ```

This will set up and deploy your Streamlit app on the AWS EC2 instance.