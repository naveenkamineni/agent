# if you running any application on aws ec2-machine make sure to provide permission in ec2 inbound rules
Your EC2 instance must allow inbound traffic on port 5000.

1️⃣ Go to AWS Console → EC2 → Security Groups

2️⃣ Find the security group attached to your EC2 instance

3️⃣ Edit Inbound Rules → Add a Rule:

Type: Custom TCP
Port Range: 5000
Source: 0.0.0.0/0 (or your IP for security)
click save
# make sure you have installed Docker on ec2 machine
###### commands to install docker on ec2 ##########

Note:when using Amazon Linux Machine

sudo yum update -y

sudo yum install docker -y

sudo service docker start

sudo usermod -aG docker ec2-user

# To check Docker installed successfully
docker ps

CONTAINER ID     IMAGE        COMMAND             CREATED            STATUS            PORTS 
# To run this agent bot on Docker
Step 1: git clone repo
git clone https://github.com/naveenkamineni/agent.git
# move directory
cd agent

<img width="170" alt="image" src="https://github.com/user-attachments/assets/7fabacba-5d0d-4e1f-a284-176e73130689" />

# make sure you have OpenRouter Deepseek-V3 0342 API on .env file

.env/

OPENROUTER_API_KEY = ""

# write docker build command to build image using Docker file 
Note: Once's you are in correct folder agent/

Command : Docker build --no-cache -t deepseek .

# Run Container from docker image build from Dockerfile
docker run -itd --name deepseek-agent -p 5008:5000 deepseek

# to move into the running docker container

[ec2-user@ip-10-230-186-188 ~]$ docker ps
CONTAINER ID   IMAGE      COMMAND           CREATED          STATUS          PORTS                                       NAMES
ee9048031e75   deepseek   "python app.py"   34 minutes ago   Up 34 minutes   0.0.0.0:5007->5000/tcp, :::5007->5000/tcp   deepseek-agent
[ec2-user@ip-10-230-186-188 ~]$ docker exec -it deepseek-agent sh
# ls
Dockerfile  README.md  __pycache__  app.py  config.py  requirements.txt  templates

# To check deepseek-agent app running on web browser

http://{ec2-machine-ip}:5008/

# if you face any issue to see app html UI on web browser check container running on docker

Command : docker ps

# if conatiner is not running on docker check logs

Command : docker logs deepseek-agent

# debug until you see this UI

<img width="741" alt="image" src="https://github.com/user-attachments/assets/e34e1dec-e24a-4f41-862f-af23096e8bd4" />




