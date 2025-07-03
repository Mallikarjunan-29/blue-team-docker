Blue-team-lab — Cloud Security Logging & Detection Playground
Welcome to blue-team-lab — a modular, Dockerized security lab for ingesting, parsing, and detecting AWS CloudTrail events using Splunk.

This is a barebone-but-powerful repo. Ideal for anyone looking to build a Blue Team detection lab from scratch — without relying on prebuilt SIEM apps.

What This Lab Does
✅ Ingests AWS CloudTrail logs from S3
✅ Uses a Python + Boto3 script to pull logs regularly via cron
✅ Parses CloudTrail JSON with a custom props.conf
✅ Mounts as a Splunk App using Docker
✅ Sets up a triggered alert to catch suspicious IAM events
✅ Modular repo: Easily expandable to include GuardDuty, Azure, GCP, SOAR (n8n), etc.

Project Structure

blue-team-docker/
├── config
│   ├── default
│   │   ├── app.conf
│   │   ├── indexes.conf
│   │   ├── inputs.conf
│   │   └── props.conf
│   └── metadata
│       └── default.meta
├── Cronlog
├── docker-compose.yml
├── README.md
├── setup-cron.sh
└── splunk
    ├── README
    ├── scripts
    │   ├── boto_guardduty_pull_logs.py
    │   ├── gcp_pull_logs.py
    │   └── s3_pull_logs.py
    └── splunk_logs
        ├── aws
        ├── gcplogs
        └── guardduty

## Dependencies##

Install Docker in Ubuntu 

Python 3.x

boto3, botocore

## Install Python:##

sudo apt install python
sudo apt update
sudo apt upgrade

## Install boto3:##

pip install boto3

## AWS CLI Configuration ##

Configure AWS account which will connect with buckers for pulling data using script.
1 - install aws cli

curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install

2- aws configure ( for configuring the aws read only user which would connect with buckets to pull data)

## Configure Google cloud account ##

sudo pip install google-cloud-storage
sudo snap install google-cloud-sdk --classic
gcloud auth application-default login
gcloud auth application-default set-quota-project Project_Name


🛠️ How to Run This Lab

## 1. Clone the Repo from the home directory ##
git clone https://github.com/Mallikarjunan-29/blue-team-docker.git

cd blue-team-docker

## Provide execution access to cron ##
chmod +x setup-cron.sh

## Execute the cron setup
./setup-cron.sh

## Start Splunk Container##

docker compose up -d

Access Splunk at: https://localhost:8000 

Login with: 👤 admin
 🔐 Password in the docker compose file

## Splunk is set up. Now fire all queries you need , create alerts and blue- team to your hearts content##


🙌 Credits Created by Mallikarjunan K (Arjun) 
Cybersecurity | SOC | Blue Team | DevSecOps 2025 

Edition# blue-team-docker
