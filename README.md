To deploy your Streamlit app on an AWS Ubuntu instance using the provided GitHub repository, follow these steps:

### Step 1: Set Up an AWS EC2 Instance
1. **Launch an AWS EC2 Instance**:
    - Go to the [AWS Management Console](https://aws.amazon.com/console/).
    - Launch a new EC2 instance.
    - Select an Ubuntu Server 20.04 LTS (or newer) Amazon Machine Image (AMI).
    - Choose an instance type (t2.micro should be sufficient for testing purposes).
    - Configure security groups to allow HTTP (port 80) and SSH (port 22) access.


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


