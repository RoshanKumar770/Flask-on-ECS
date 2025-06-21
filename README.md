# 🚀 Flask App on AWS ECS (Fargate)

A lightweight Dockerized **Flask** web application deployed using **Amazon ECS (Fargate)**. This project demonstrates how to containerize a Python web app, push it to **Amazon ECR**, and deploy it to a scalable, serverless container environment using ECS and Fargate.


- **Flask**: Python web framework
- **Docker**: Containerization platform
- **Amazon ECR**: Stores the Docker image
- **Amazon ECS (Fargate)**: Deploys the container
- **ALB**: (Optional) Load balancer to route traffic

## 📦 Features

- 🐳 Lightweight Docker image (Python 3.12-slim)
- 🔁 Dynamic routing with `/greet/<name>`
- ☁️ Serverless container orchestration via AWS Fargate
- 🚪 Exposes the app on port `3000`
  
