🛡️ Blue-Team Lab: Cloud Logging & Detection Playground

A modular, Dockerized detection lab for ingesting, parsing, and automating AWS + GCP logs into Splunk — built from scratch, no prebuilt SIEM apps, no fluff.

Ideal for SOC analysts, blue teamers, and detection engineers who want to understand every moving part of log ingestion and parsing in a real-world home lab.


---

🔍 What This Lab Does

✅ Ingests AWS CloudTrail logs from S3
✅ Pulls GuardDuty and GCP Audit logs via Python scripts
✅ Uses cron jobs to automate ingestion
✅ Parses logs using props.conf, inputs.conf, and indexes.conf
✅ All config lives inside a Splunk App, mounted via Docker
✅ Fully modular — easily extendable to other cloud providers or sources
✅ Minimalist but powerful: no GUI bloat, just raw detection muscle


---

📁 Project Structure

blue-team-docker/
├── config/
│   ├── default/
│   │   ├── app.conf
│   │   ├── indexes.conf
│   │   ├── inputs.conf
│   │   └── props.conf
│   └── metadata/default.meta
├── Cronlog/
├── docker-compose.yml
├── setup-cron.sh
├── splunk/
│   ├── README
│   ├── scripts/
│   │   ├── boto_guardduty_pull_logs.py
│   │   ├── gcp_pull_logs.py
│   │   └── s3_pull_logs.py
│   └── splunk_logs/
│       ├── aws/
│       ├── gcplogs/
│       └── guardduty/
└── README.md


---

⚙️ Dependencies

Python 3.x

Docker

boto3, botocore, and google-cloud-storage Python packages

GCP CLI (gcloud) + AWS CLI configured with least-privilege access


Install Python:

sudo apt update && sudo apt install python3 python3-pip -y

Install Boto3:

pip3 install boto3 botocore

Install GCP SDK:

sudo pip install google-cloud-storage
sudo snap install google-cloud-sdk --classic


---

💪 AWS CLI Setup

1. Install AWS CLI:



curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install

2. Configure it:



aws configure

Use read-only credentials for pulling logs from S3 buckets.


---

☁️ GCP CLI Setup

gcloud auth application-default login
gcloud auth application-default set-quota-project <YOUR_PROJECT_NAME>


---

🚀 Running the Lab

git clone https://github.com/Mallikarjunan-29/blue-team-docker.git
cd blue-team-docker

chmod +x setup-cron.sh
./setup-cron.sh  # sets up cron job to pull logs

docker compose up -d  # starts Splunk with mounted config

Access Splunk at 👉 https://localhost:8000
Login: admin / password from docker-compose.yml


---

🌟 Like it? Star it. Use it. Fork it.

This project is open-source and built to be extended. If it helps you learn or speeds up your detection engineering workflow:

🔗 Give it a star
👁️ Fork and remix it
🔧 Open issues or improvements — collaboration welcome


---

👨‍💼 Created By

Mallikarjunan K (Arjun)
Cybersecurity | SOC | Blue Team | DevSecOps
2025 Edition — blue-team-docker

