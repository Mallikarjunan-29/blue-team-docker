🛡️ blue-team-lab — Cloud Security Logging & Detection Playground
Welcome to blue-team-lab — a modular, Dockerized security lab for ingesting, parsing, and detecting AWS CloudTrail events using Splunk.

This is a barebone-but-powerful repo. Ideal for anyone looking to build a Blue Team detection lab from scratch — without relying on prebuilt SIEM apps.

🚀 What This Lab Does
✅ Ingests AWS CloudTrail logs from S3
✅ Uses a Python + Boto3 script to pull logs regularly via cron
✅ Parses CloudTrail JSON with a custom props.conf
✅ Mounts as a Splunk App using Docker
✅ Sets up a triggered alert to catch suspicious IAM events
✅ Modular repo: Easily expandable to include GuardDuty, Azure, GCP, SOAR (n8n), etc.

📦 Project Structure

── blue-team-docker
 ── config 
│   ├── default 
│   │   ├── app.conf 
│   │   ├── indexes.conf 
│   │   ├── inputs.conf 
│   │   └── props.conf 
│   └── metadata 
│   └── default.meta 
├── docker-compose.yml 
└── splunk 
├── README 
├── scripts 
│   └── s3_pull_logs.py 
└── splunk_logs 
     └── aws

🛠️ How to Run This Lab

1. Clone the Repo
git clone https://github.com/Mallikarjunan-29/blue-team-docker.git

cd blue-team-docker

Start Splunk Container

docker compose up -d

should be executed from the folder where docker_compose.yml file is present

Access Splunk at: https://localhost:8000 

Login with: 👤 admin
 🔐 blueteamlab@123

Pull Logs from S3 Configure AWS credentials (~/.aws/credentials)
Use s3_pull_logs.py to download logs to /data/ingest/aws

Cron runs every 6 minutes to pull logs as per below setting. Please use the setting that fits your style

*/6 * * * * /usr/bin/python3 /home//blue-team-docker/splunk/scripts/s3_pull_logs.py >> /home/cronlogs/cron.log

the path to s2_pull_logs.py from the docker is the second section

create the cronlogs folder in home directory 

Alerting Use Case Configured to catch suspicious IAM activity:

index="aws-log" | spath input=_raw path=Records{} output=record | mvexpand record | spath input=record path=eventName output=event | spath input=record path=userIdentity.arn output=user_arn | spath input=record path=eventTime output=Timestamp | spath input=record path=sourceIPAddress output=SourceIP | search event IN ("Create*", "Delete*", "Attach*") | eval is_assumed_role=if(match(user_arn, "assumed-role"), "yes", "no") | search is_assumed_role="no" | table Timestamp, SourceIP, user_arn, event

📌 Dependencies Docker

Splunk Enterprise Docker image

Python 3.x

boto3, botocore

Install boto3:

pip install boto3

Do this before setting up the cron


🙌 Credits Created by Mallikarjunan K (Arjun) 
Cybersecurity | SOC | Blue Team | DevSecOps 2025 

Edition# blue-team-docker