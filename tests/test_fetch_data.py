import unittest
from unittest.mock import patch, MagicMock
from scripts.fetch_data import fetch_projects, fetch_project_versions, fetch_updated_issues, fetch_issue_details, fetch_audit_history

class TestFetchData(unittest.TestCase):

    @patch('scripts.fetch_data.requests.get')
    def test_fetch_projects(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'data': [{'id': 1, 'name': 'Project1', 'updated': '2024-01-01T00:00:00Z'}]}
        mock_get.return_value = mock_response
        
        projects = fetch_projects()
        self.assertEqual(len(projects), 1)
        self.assertEqual(projects[0]['name'], 'Project1')

    @patch('scripts.fetch_data.requests.get')
    def test_fetch_project_versions(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'data': [{'id': 1, 'name': 'Version1', 'updated': '2024-01-01T00:00:00Z'}]}
        mock_get.return_value = mock_response
        
        versions = fetch_project_versions(1)
        self.assertEqual(len(versions), 1)
        self.assertEqual(versions[0]['name'], 'Version1')

    @patch('scripts.fetch_data.requests.get')
    def test_fetch_updated_issues(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'data': [{'issueId': 1, 'lastUpdateDate': '2024-01-01T00:00:00Z'}]}
        mock_get.return_value = mock_response
        
        issues = fetch_updated_issues(1, '2023-01-01T00:00:00Z')
        self.assertEqual(len(issues), 1)
        self.assertEqual(issues[0]['issueId'], 1)

    @patch('scripts.fetch_data.requests.get')
    def test_fetch_issue_details(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'issueId': 1, 'lastUpdateDate': '2024-01-01T00:00:00Z'}
        mock_get.return_value = mock_response
        
        details = fetch_issue_details(1)
        self.assertEqual(details['issueId'], 1)

    @patch('scripts.fetch_data.requests.get')
    def test_fetch_audit_history(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'data': [{'id': 1, 'lastUpdateDate': '2024-01-01T00:00:00Z'}]}
        mock_get.return_value = mock_response
        
        audits = fetch_audit_history(1)
        self.assertEqual(len(audits), 1)
        self.assertEqual(audits[0]['id'], 1)

if __name__ == '__main__':
    unittest.main()
