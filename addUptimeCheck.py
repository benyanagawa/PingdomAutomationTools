import os
import requests
import json
import csv

from config import headers, csv_file_name

def add_check(name, host, resolution=5, check_type='http', url="/", shouldnotcontain="Error", encryption=True):
    print(f"start add check {name}")
    data = {
        "host": host,
        "name": name,
        "type": check_type,
        # "auth": "",
        # "custom_message": "",
        "encryption": encryption,
        # "integrationids": [],
        # "ipv6": false,
        # "notifyagainevery": 0,
        # "notifywhenbackup": true,
        "paused": True,
        # "port": 80,
        # "postdata": postdata,
        # "probe_filters": probe_filters,
        # "requestheaders": requestheaders,
        "resolution": resolution,
        # "responsetime_threshold": 30000,
        # "sendnotificationwhendown": 2,
        # "shouldcontain": shouldcontain,
        "shouldnotcontain": shouldnotcontain,
        # "ssl_down_days_before": 0,
        # "tags": "",
        # "teamids": 1,2,
        "url": url,
        # "userids": userids,
        # "verify_certificate": verify_certificate,
    }

    print(f"Adding check {name} with data: {data}")

    response = requests.post('https://api.pingdom.com/api/3.1/checks', headers=headers, data=data)
    if response.status_code == 200:
        print(f"Check {name} added successfully")
    else:
        print(f"Failed to add check {name}: {response.text}")

current_dir = os.path.dirname(os.path.abspath(__file__))
csv_file_path = os.path.join(current_dir, csv_file_name)

print(f"Reading file {csv_file_path}")

with open(csv_file_path, mode='r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        encryption = True if row['encryption'].lower() == 'true' else False
        add_check(row['name'], row['host'], int(row['resolution']), row['type'], row['url'], row['shouldnotcontain'], encryption)
