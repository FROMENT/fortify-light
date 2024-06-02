import requests

def generate_auth_token(ssc_url, username, password):
    url = f"{ssc_url}/api/v1/tokens"
    response = requests.post(url, auth=(username, password))
    if response.status_code == 201:
        return response.json()['data']['token']
    else:
        raise Exception(f"Failed to generate token: {response.status_code} - {response.text}")