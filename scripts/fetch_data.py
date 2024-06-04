import requests
import os
import logging
from scripts.encrypt import decrypt_data, load_key
from dotenv import load_dotenv
from scripts.process_csv import issues_to_csv

# Configurer le journal de logs
logging.basicConfig(filename='fortify_light.log', level=logging.DEBUG, 
                    format='%(asctime)s %(levellevel)s %(message)s')

# Charger les variables d'environnement
load_dotenv()

# Configuration à partir des variables d'environnement
SSC_URL = os.getenv('SSC_URL')
ENC_AUTH_TOKEN = os.getenv('SSC_AUTH_TOKEN')

# Décrypter le token
key = load_key('encryption.key')
AUTH_TOKEN = decrypt_data(ENC_AUTH_TOKEN.encode(), key)

# En-têtes pour l'authentification
headers = {
    'Authorization': f'FortifyToken {AUTH_TOKEN}',
    'Content-Type': 'application/json'
}

def fetch_projects():
    url = f"{SSC_URL}/api/v1/projects"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get('data', [])
    else:
        logging.error(f"Error: {response.status_code} - {response.text}")
        return None

def fetch_project_versions(project_id):
    url = f"{SSC_URL}/api/v1/projects/{project_id}/versions"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get('data', [])
    else:
        logging.error(f"Error: {response.status_code} - {response.text}")
        return None

def fetch_updated_issues(project_version_id, last_update_date):
    url = f"{SSC_URL}/api/v1/projectVersions/{project_version_id}/issues"
    params = {'q': f'lastUpdateDate:>{last_update_date}'}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        issues = response.json().get('data', [])
        issues_to_csv(issues, 'data/vulnerabilities.csv')
        return issues
    else:
        logging.error(f"Error: {response.status_code} - {response.text}")
        return None

def fetch_issue_details(issue_id):
    url = f"{SSC_URL}/api/v1/issues/{issue_id}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        logging.error(f"Error: {response.status_code} - {response.text}")
        return None

def fetch_audit_history(issue_id):
    url = f"{SSC_URL}/api/v1/issues/{issue_id}/auditHistory"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get('data', [])
    else:
        logging.error(f"Error: {response.status_code} - {response.text}")
        return None
