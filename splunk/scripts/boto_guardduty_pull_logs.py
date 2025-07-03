import boto3
import json
import os

ACCOUNT_ID = '002125562743' # use your account id from aws
REGIONS = ['us-east-1', 'us-east-2']
DEST_FOLDER = os.path.expanduser('~/blue-team-docker/splunk/splunk_logs/guardduty')

def fetch_guardduty_findings(region):
    print(f"\n🔍 Fetching GuardDuty findings in {region}...")
    gd_client = boto3.client('guardduty', region_name=region)

    detectors = gd_client.list_detectors()['DetectorIds']
    if not detectors:
        print(f"❌ No GuardDuty detector found in {region}. Maybe GuardDuty isn't enabled here.")
        return
    
    detector_id = detectors[0]

    findings = []
    paginator = gd_client.get_paginator('list_findings')
    page_iterator = paginator.paginate(DetectorId=detector_id)

    for page in page_iterator:
        finding_ids = page['FindingIds']
        if not finding_ids:
            continue
        response = gd_client.get_findings(DetectorId=detector_id, FindingIds=finding_ids)
        findings.extend(response['Findings'])

    if findings:
        os.makedirs(DEST_FOLDER, exist_ok=True)
        file_path = os.path.join(DEST_FOLDER, f'guardduty_findings_{region}.json')
        with open(file_path, 'w') as f:
            json.dump(findings, f, indent=2, default=str)
        print(f"✅ Saved {len(findings)} findings to {file_path}")
    else:
        print(f"ℹ️ No findings found in {region} at this time.")

if __name__ == "__main__":
    for region in REGIONS:
        fetch_guardduty_findings(region)
