# VentureGen
A LangChain and OpenAI GPT 3.5 powered app to brainstorm Startup name and pitch

Checkout the deployed app in action: [http://ec2-40-176-10-24.ca-west-1.compute.amazonaws.com:8501](http://ec2-40-176-10-24.ca-west-1.compute.amazonaws.com:8501)

This readme will focus only on the **app deployment instructions**. For more details, please read the blog for this app [here](https://apsinghanalytics.github.io/2023/12/23/VentureForge_A_LangchainApp/)

This streamlit app was deployed to an ec2 instance following the instructions in Rahul Agarwal's blog, which you can find [here](https://towardsdatascience.com/how-to-deploy-a-streamlit-app-using-an-amazon-free-ec2-instance-416a41f69dc3)

There were additonal changes required, which are listed below:

### Install Additional Libraries

The command pip install plotly_express is not required. However, the following libraries should be installed on your EC2 instance:

pip install streamlit

pip install st-annotated-text

pip install langchain

pip install openai

### Error Connecting by SSH 

If you start getting the following error, especially when using a WSL (Windows Subsystem for Linux)

**"It is required that your private key files are NOT accessible by others. This private key will be ignored"**

then copy the pem file from the folder in which it was placed to the root of the WSH by the following command:

**cp /mnt/c/AWS/streamlitapp.pem ~/** 

Note: In my case, the PEM file for Windows was located at 'C:\AWS\streamlitapp.pem'. Additionally, the file was named 'streamlitapp.pem'.

then move to the root directory of the WSL by: 

**cd ~**

then apply:

**chmod 400 streamlitapp.pem**

The idea is to restrict the permissions of the pem file by making it read-only for security reasons. This should allow the private keys in this file to work via the SSH protocol. Then simply continue with the next steps listed in the blog: 

**ssh -i "streamlitapp.pem" ubuntu@ec2-instance-public-ip**

### Transfering the API Credentials File to the EC2 Instance

Once the git clone of the repo is done, the **creds.py** file with the API key will be required to run the app. Cloning will not copy this file because it is listed in  the.gitignore file

copy paste your creds.py file in a folder in c drive in Windows (say "C:\AWS\") and then use the following command to copy it to the root directory of your WSL

**cp /mnt/c/aws/creds.py ~/**

Then use scp protocol to do a **secure copy**:

**scp -i /path/to/your-key.pem /path/to/local/file ubuntu@ec2-instance-public-ip:~/path/to/remote/directory**

which translate to the following in my case (use your instance's public ip):

**scp -i streamlitapp.pem creds.py ubuntu@ec2-instance-public-ip:~/streamlit_VentureGen/**

### Generate the requirements.txt

once logged in to the ec2 instance session, move to the streamlit_VentureGen using:

**cd streamlit_VentureGen**

and then do the following:

**pip freeze > requirements.txt**

which should create a requirements.txt inside the streamlit_VentureGen folder. This can then be transferred back to WSL by SCP protocol.


