To deploy your Streamlit app on an AWS Ubuntu instance using the provided GitHub repository, follow these steps:

### Step 1: Set Up an AWS EC2 Instance
1. **Launch an AWS EC2 Instance**:
    - Go to the [AWS Management Console](https://aws.amazon.com/console/).
    - Launch a new EC2 instance.
    - Select an Ubuntu Server 20.04 LTS (or newer) Amazon Machine Image (AMI).
    - Choose an instance type (t2.micro should be sufficient for testing purposes).
    - Configure security groups to allow HTTP (port 80) and SSH (port 22) access.



### Full Script for Automation
You can create a shell script to automate these steps:

```sh
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

# Run the Streamlit app
echo "Running the Streamlit app..."
streamlit run app.py --server.port 8501
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


