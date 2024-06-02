import requests
import os
from scripts.encrypt import decrypt_data, load_key
from dotenv import load_dotenv
from scripts.process_csv import issues_to_csv

# Load environment variables
load_dotenv()

# Configuration from environment variables
SSC_URL = os.getenv('SSC_URL')
ENC_AUTH_TOKEN = os.getenv('SSC_AUTH_TOKEN')

# Decrypt the token
key = load_key('encryption.key')
AUTH_TOKEN = decrypt_data(ENC_AUTH_TOKEN.encode(), key)

# Headers for authentication
headers = {
    'Authorization': f'FortifyToken {AUTH_TOKEN}',
    'Content-Type': 'application/json'
}

# Function to fetch all projects
def fetch_projects():
    url = f"{SSC_URL}/api/v1/projects"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get('data', [])
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

# Function to fetch all versions of a project
def fetch_project_versions(project_id):
    url = f"{SSC_URL}/api/v1/projects/{project_id}/versions"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get('data', [])
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

# Function to fetch updated issues of a project version since a specific date
def fetch_updated_issues(project_version_id, last_update_date):
    url = f"{SSC_URL}/api/v1/projectVersions/{project_version_id}/issues"
    params = {'q': f'lastUpdateDate:>{last_update_date}'}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        issues = response.json().get('data', [])
        issues_to_csv(issues, 'data/vulnerabilities.csv')
        return issues
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None