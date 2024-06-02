import requests
import os

# Configuration from environment variables
SSC_URL = os.getenv('SSC_URL', 'https://fortify-dev.tools.sap/ssc')
AUTH_TOKEN = os.getenv('SSC_AUTH_TOKEN', 'your-auth-token')

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
        return response.json().get('data', [])
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None