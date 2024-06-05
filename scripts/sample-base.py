import requests
import json
from datetime import datetime, timedelta

# Remplacez ces variables par vos informations
base_url = 'https://fortify-dev.tools.sap/ssc/api/v1'
username = 'your_username'
password = 'your_password'

# Fonction pour obtenir un token d'authentification
def get_auth_token():
    url = f'{base_url}/tokens'
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    data = {
        'userName': username,
        'password': password
    }
    response = requests.post(url, headers=headers, data=json.dumps(data))
    response.raise_for_status()
    return response.json()['data']['token']

# Fonction pour récupérer les projets
def get_projects(token):
    url = f'{base_url}/projects'
    headers = {
        'Authorization': f'FortifyToken {token}',
        'Accept': 'application/json'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()['data']

# Fonction pour récupérer les versions d'un projet
def get_project_versions(token, project_id):
    url = f'{base_url}/projects/{project_id}/versions'
    headers = {
        'Authorization': f'FortifyToken {token}',
        'Accept': 'application/json'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()['data']

# Fonction pour récupérer les vulnérabilités avec les filtres nécessaires
def get_filtered_vulnerabilities(token, version_id, last_update_date):
    url = f'{base_url}/issues'
    headers = {
        'Authorization': f'FortifyToken {token}',
        'Accept': 'application/json'
    }
    params = {
        'start': 0,
        'limit': 100,  # Ajustez la limite en fonction de vos besoins
        'q': f"lastScanDate:>{last_update_date} AND (severity:'Critical' OR severity:'High' OR severity:'Medium') AND projectVersionId:{version_id}"
    }
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()['data']

# Fonction principale
def main():
    try:
        token = get_auth_token()
        
        # Définir la date de la dernière mise à jour (une semaine en arrière)
        last_update_date = (datetime.now() - timedelta(weeks=1)).strftime('%Y-%m-%dT%H:%M:%SZ')
        
        # Récupérer la liste des projets
        projects = get_projects(token)
        
        for project in projects:
            project_id = project['id']
            project_name = project['name']
            
            # Récupérer les versions de chaque projet
            versions = get_project_versions(token, project_id)
            
            for version in versions:
                version_id = version['id']
                version_name = version['name']
                
                # Récupérer les vulnérabilités pour chaque version
                vulnerabilities = get_filtered_vulnerabilities(token, version_id, last_update_date)
                
                for vulnerability in vulnerabilities:
                    print(f"Project: {project_name}, Version: {version_name}, "
                          f"ID: {vulnerability['issueInstanceId']}, "
                          f"Severity: {vulnerability['severity']}, "
                          f"Type: {vulnerability['kingdom']}, "
                          f"Audit Status: {vulnerability['auditStatus']}, "
                          f"Remediation Status: {vulnerability['remediationStatus']}")
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    except Exception as err:
        print(f"Other error occurred: {err}")

if __name__ == '__main__':
    main()
