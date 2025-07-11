🛡️ Blue-Team Lab: Cloud Logging & Detection Playground

A modular, Dockerized detection lab for ingesting, parsing, and automating AWS + GCP logs into Splunk — built from scratch, no prebuilt SIEM apps, no fluff.

Ideal for SOC analysts, blue teamers, and detection engineers who want to understand every moving part of log ingestion and parsing in a real-world home lab.


---

🔍 What This Lab Does

✅ Ingests AWS CloudTrail logs directly from S3
✅ Pulls GuardDuty and GCP Audit Logs using custom Python scripts
✅ Automates ingestion with cron jobs — fully hands-off
✅ Parses logs using props.conf, inputs.conf, and indexes.conf — Splunk-native
✅ All Splunk config lives inside a Docker-mounted custom app
✅ Fully modular — plug in any cloud provider or log source
✅ Now includes Splunk + n8n in a single Docker Compose stack
✅ Sends real-time alerts via Telegram and Gmail from Splunk using n8n

This isn’t a “SIEM toy.”
It’s a practical blueprint for building a real-world detection pipeline.



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
Docker

Python 3.x

AWS CLI

GCP CLI (gcloud)

Python packages:

bash
Copy
Edit
pip install boto3 botocore google-cloud-storage
☁️ Cloud Setup (Quick)
AWS CLI
bash
Copy
Edit
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
aws configure
Use read-only credentials to pull from S3/GuardDuty.

GCP SDK
bash
Copy
Edit
sudo snap install google-cloud-sdk --classic
gcloud auth application-default login
gcloud auth application-default set-quota-project <YOUR_PROJECT_NAME>
🚀 How to Run the Lab
bash
Copy
Edit
git clone https://github.com/Mallikarjunan-29/blue-team-docker.git
cd blue-team-docker
chmod +x setup-cron.sh
./setup-cron.sh
docker compose up -d
➡️ Access Splunk: https://localhost:8000
➡️ Access n8n: http://localhost:5678
(Default credentials are in the docker-compose.yml)

📬 What’s New
🔁 Alerting with n8n
This update adds workflow-based alerting with n8n, a powerful open-source automation tool:

✅ Real-time Telegram alerts for specific Splunk detections

✅ Gmail notifications with contextual event info

✅ Easily extendable to Slack, Discord, Teams, webhooks, or SIEMs

👨‍💻 Ideal Use Cases
Blue Teamers building a home lab with full control over detection paths

Detection engineers writing custom detections with real alert triggers

SOC analysts preparing for interviews or showing off cloud-native detection skills

GRC pros learning log pipelines from scratch

🌟 Like It? Fork It. Extend It.
This is a detection engineer’s playground, not a black box. If it helps you:

⭐ Star the repo

🍴 Fork and remix it

🛠️ Contribute ideas or PRs

📣 Share it with fellow blue teamers

👨‍🏫 Built By
Mallikarjunan K (Arjun)
SOC & Cloud Security | Detection Engineering | DevSecOps
LinkedIn | Medium | 2025 Edition


