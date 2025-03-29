# if you running any application on aws ec2-machine make sure to provide permission in ec2 inbound rules
Your EC2 instance must allow inbound traffic on port 5000.

1️⃣ Go to AWS Console → EC2 → Security Groups

2️⃣ Find the security group attached to your EC2 instance

3️⃣ Edit Inbound Rules → Add a Rule:

Type: Custom TCP
Port Range: 5000
Source: 0.0.0.0/0 (or your IP for security)
click save
# make sure you have Docker on ec2 machine
###### commands to install docker on ec2 ##########

Note:when using Amazon Linux Machine

sudo yum update -y

sudo yum install docker -y

sudo service docker start

sudo usermod -aG docker ec2-user

# To check Docker installed successfully
docker ps
######### You will see #############
CONTAINER ID   IMAGE      COMMAND           CREATED          STATUS          PORTS 
# To run this agent bot on Docker
Step 1: git clone repo
git clone https://github.com/naveenkamineni/agent.git
# move directory
cd agent
<img width="170" alt="image" src="https://github.com/user-attachments/assets/7fabacba-5d0d-4e1f-a284-176e73130689" />
# write docker build command to build image using Docker file 
Note: Once's you are in correct folder agent/
To check you are correct folder Type pwd(you see path) or ls( you can see project files)

Docker build --no-cache -t deepseek .
# Run Container from docker image build from Dockerfile
docker run -itd --name deepseek-agent -p 5008:5000 deepseek


