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
📌 Dependencies Docker

Splunk Enterprise Docker image

Python 3.x

boto3, botocore

Install Python:

sudo apt install python
sudo apt update
sudo apt upgrade

Install boto3:

pip install boto3

Configure AWS account which will connect with buckers for pulling data using script.
1 - install aws cli

curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install

2- aws configure ( for configuring the aws read only user which would connect with buckets to pull data)

update the boto scripts

in the script boto_guardduty_pull_logs.py - Update your aws account id
in the script s3_pull_logs.py - update your aws account id and bucker name

Pull Logs from S3 Configure AWS credentials (~/.aws/credentials)
Use s3_pull_logs.py to download logs to /data/ingest/aws
Use boto_guardduty_pull_logs.py to download logs to /data/ingest/guardduty

Cron runs every 6 minutes to pull logs as per below setting. Please use the setting that fits your style

*/6 * * * * /usr/bin/python3 /home/blue-team-docker/splunk/scripts/s3_pull_logs.py >> /home/blue-team-docker/cronlogs/s3.log
*/6 * * * * /usr/bin/python3 /home/blue-team-docker/splunk/scripts/boto_guardduty_pull_logs.py >> /home/blue-team-docker/cronlogs/guardduty.log

##e path for the script file should be the one where the script is present from the home directory. If git clone is run from the home directory then the above path would be enough##

🛠️ How to Run This Lab

1. Clone the Repo
git clone https://github.com/Mallikarjunan-29/blue-team-docker.git

cd blue-team-docker

Start Splunk Container

docker compose up -d

should be executed from the folder where docker_compose.yml file is present

Access Splunk at: https://localhost:8000 

Login with: 👤 admin
 🔐 Password in the docker compose file


Alerting Use Case Configured to catch suspicious IAM activity:

index="aws-log" | spath input=_raw path=Records{} output=record | mvexpand record | spath input=record path=eventName output=event | spath input=record path=userIdentity.arn output=user_arn | spath input=record path=eventTime output=Timestamp | spath input=record path=sourceIPAddress output=SourceIP | search event IN ("Create*", "Delete*", "Attach*") | eval is_assumed_role=if(match(user_arn, "assumed-role"), "yes", "no") | search is_assumed_role="no" | table Timestamp, SourceIP, user_arn, event



🙌 Credits Created by Mallikarjunan K (Arjun) 
Cybersecurity | SOC | Blue Team | DevSecOps 2025 

Edition# blue-team-docker
