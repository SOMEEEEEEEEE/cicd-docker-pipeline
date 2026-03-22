# Web Demo – CI/CD & Container Deployment

A simple Flask-based web service demonstrating containerization, CI/CD workflows, and multi-service deployment using Docker Compose and Nginx.

---

## Overview

This project evolves from a single-container Flask application to a multi-service architecture:

- Flask application (Python)
- Docker containerization
- GitHub Actions CI/CD pipeline
- Nginx reverse proxy
- Docker Compose orchestration

---

## Architecture

Client → EC2 → Nginx (container) → Web Service (container)

- Nginx routes traffic to the internal service
- Containers communicate via Docker network

---

## Tech Stack

- Python (Flask)
- Docker
- Docker Compose
- Nginx
- GitHub Actions (CI/CD)

---

## How to Run Locally / EC2 

### 1. Start services 

```bash
docker-compose up -d --build
```

### 2. Access service

http://<EC2-PUBLIC-IP>

or 

http://localhost

---


