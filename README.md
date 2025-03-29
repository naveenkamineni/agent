# Deploying DeepSeek-Agent on AWS EC2 with Docker

## 🚀 Prerequisites
Before deploying the **DeepSeek-Agent** on your AWS EC2 instance, ensure the following:

✅ You have an **AWS EC2 instance** running (Amazon Linux recommended).  
✅ **Docker** is installed on the EC2 instance.  
✅ **Security group** allows inbound traffic on port **5008**.  
✅ **OpenRouter API Key** is available in a `.env` file.

---

## 🔹 Step 1: Configure EC2 Security Group

Your EC2 instance must allow inbound traffic on **port 5008** to access the application via a web browser.

1️⃣ Navigate to **AWS Console → EC2 → Security Groups**.  
2️⃣ Locate the security group associated with your EC2 instance.  
3️⃣ Click **Edit Inbound Rules** → **Add Rule**:
   - **Type**: Custom TCP
   - **Port Range**: **5008**
   - **Source**: `0.0.0.0/0` (or specify your IP for better security)
4️⃣ Click **Save Rules**.

---

## 🔹 Step 2: Install Docker on EC2 (Amazon Linux)
Run the following commands to install Docker:
```bash
sudo yum update -y
sudo yum install docker -y
sudo service docker start
sudo usermod -aG docker ec2-user
```

✅ **Verify Docker installation:**
```bash
docker ps
```

---

## 🔹 Step 3: Clone the DeepSeek-Agent Repository

```bash
git clone https://github.com/naveenkamineni/agent.git
cd agent
```

✅ Ensure you have the **OpenRouter API Key** in the `.env` file:
```
.env/
OPENROUTER_API_KEY = "your-api-key"
```

---

## 🔹 Step 4: Build and Run the Docker Container

1️⃣ **Build the Docker Image**
```bash
docker build --no-cache -t deepseek .
```

2️⃣ **Run the Container**
```bash
docker run -itd --name deepseek-agent -p 5008:5000 deepseek
```

---

## 🔹 Step 5: Verify the Running Container

Check if the container is running:
```bash
docker ps
```

If the container is not running, check logs for errors:
```bash
docker logs deepseek-agent
```

To enter the running container:
```bash
docker exec -it deepseek-agent sh
```

---

## 🔹 Step 6: Access DeepSeek-Agent in Browser
Once the container is running, access the application using:

🌍 `http://{EC2-PUBLIC-IP}:5008/`

💡 If you face issues:
- **Ensure Docker is running** (`docker ps`)
- **Check container logs** (`docker logs deepseek-agent`)
- **Verify security group settings** (port 5008 must be open)

---

## 🎯 Expected UI
Once the setup is successful, you should see the following UI:

![DeepSeek-Agent UI](https://github.com/user-attachments/assets/e34e1dec-e24a-4f41-862f-af23096e8bd4)

---

## ✅ Troubleshooting
If you cannot access the UI:
1. Ensure the container is running:
   ```bash
   docker ps
   ```
2. If the container is not running, check logs:
   ```bash
   docker logs deepseek-agent
   ```
3. Make sure the **EC2 security group** allows traffic on **port 5008**.
4. Restart the container if necessary:
   ```bash
   docker restart deepseek-agent
   ```

---

## 🎉 Conclusion
You have successfully deployed **DeepSeek-Agent** on an AWS EC2 instance using Docker! 🚀

🔹 **Dockerized setup for easy deployment**  
🔹 **Web-accessible AI agent**  
🔹 **Secure and scalable**  

Happy Coding! 🎯

