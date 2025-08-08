# Cloud-Based Web App Deployment & Resilience Simulation

**Project Title:** Cloud Infrastructure Project - Angeline CSE ‘A’

## 1. Overview

This project demonstrates the complete deployment of a Python Flask web application on AWS using Terraform, Jenkins, and CloudWatch. It includes setting up infrastructure as code, configuring a CI/CD pipeline, implementing monitoring and alerting, and simulating a system failure for resilience testing.

---

## 2. Architecture Overview

- AWS EC2 Instance running a Flask Web App
- Security Group allowing HTTP, HTTPS, and SSH
- IAM Role for EC2 with access to CloudWatch
- CloudWatch monitoring for metrics and logs
- SNS for alert notifications
- Jenkins pipeline for CI/CD automation
- GitHub repository as source code management

---

## 3. Terraform Script

**File:** `main.tf`

```hcl
provider "aws" {
  region = "eu-north-1"
}

resource "aws_instance" "weather_ec2" {
  ami                         = "ami-006b4a3ad5f56fbd6"
  instance_type               = "t3.micro"
  key_name                    = "WeatherAppKey"
  vpc_security_group_ids      = ["sg-09328a13b7916ba38"]
  subnet_id                   = "subnet-05f4980e60d37121e"

  tags = {
    Name = "WEATHERMAN"
  }

  user_data = <<-EOF
    yum update -y
    yum install -y python3 git
    cd /home/ec2-user
    git clone https://github.com/23f-3004447/WeatherApp.git
    cd WeatherApp
    pip3 install -r requirements.txt
    nohup python3 app.py > flask.log 2>&1 &
  EOF
}
## 4. Jenkinsfile
Pipeline script to automate deployment

groovy
Copy
Edit
pipeline {
    agent any

    stages {
        stage('Clone Repo') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/23f-3004447/WeatherApp.git',
                    credentialsId: 'a5308c41-1e1b-4839-af30-fe85ccdef2fa'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Run Flask App') {
            steps {
                sh '''
                    fuser -k 5000/tcp || true
                    nohup python3 app.py > flask.log 2>&1 &
                '''
            }
        }
    }
}


## 5. Configuration Details
IAM Role: EC2WebAppRole
Permissions: EC2, CloudWatch

Security Group: sg-09328a13b7916ba38
Inbound Rules: 22 (SSH), 80 (HTTP), 443 (HTTPS), and Flask ports (5000, 8000, etc.)

EC2 Instance Tags:
Name=WeatherAppServer, Role=WebApp

CloudWatch Agent: Configured to collect:

CPU Utilization

Network In/Out

Custom application logs (flask.log)

## 6. Monitoring and Dashboard
Service Used: Amazon CloudWatch

Metrics Tracked:

CPU Utilization

Network In/Out

Application logs (via log groups)

Custom metric for app failure

Alert Setup:

SNS Topic: arn:aws:sns:eu-north-1:789665426725:weather

CloudWatch Alarm on custom metric failure > 70 within 1 day

SNS sends notification to subscribers when alarm state = In alarm

## 7. Resilience Simulation Report
Alarm Details:

Alarm Name: failure

Metric Tracked: Custom metric failure

Condition: Value > 70 for 1 datapoint within 1 day

Trigger Time: 2025-06-09 18:29:48 (Local Time)

Alarm History:

2025-06-09 18:09:01 – Alarm created

2025-06-09 18:29:48 – Alarm transitioned to In alarm

SNS Action:

Notification sent to weather topic

No auto-remediation configured

Admin Response:

Manual inspection of Flask logs

Identified abnormal spike in values

Flask service restarted manually

## 8. Conclusion
This project demonstrates:

✅ Full infrastructure provisioning using Terraform

✅ CI/CD pipeline setup with Jenkins

✅ Secure and scalable AWS architecture

✅ Real-time application monitoring and alerting via CloudWatch

✅ System failure simulation and response using custom metrics and SNS

✅ Successful deployment and live hosting of a Python Flask web app

