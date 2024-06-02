from fetch_data import fetch_projects, fetch_project_versions, fetch_updated_issues
from initialize_db import initialize_database
from extract_metrics import extract_metrics
from save_metrics import save_metrics_to_db
from copy_metrics import copy_metrics_from_previous_week
import datetime
import sqlite3

def main():
    initialize_database()
    last_update_date = '2024-01-01T00:00:00Z'
    projects = fetch_projects()
    if projects is not None:
        for project in projects:
            project_id = project['id']
            versions = fetch_project_versions(project_id)
            if versions is not None:
                for version in versions:
                    version_id = version['id']
                    issues = fetch_updated_issues(version_id, last_update_date)
                    if issues is not None and len(issues) > 0:
                        metrics = extract_metrics('data/vulnerabilities.csv')
                        save_metrics_to_db(metrics, project_id, version_id)
                        save_historical_metrics(metrics, project_id, version_id)
                    else:
                        print(f"No changes for version ID: {version_id}. Copying metrics from previous week.")
                        copy_metrics_from_previous_week(project_id, version_id)
            else:
                print(f"Failed to fetch versions for project ID: {project_id}")
    else:
        print("Failed to fetch projects")

def save_historical_metrics(metrics, project_id, version_id):
    conn = sqlite3.connect('data/vulnerabilities.db')
    cursor = conn.cursor()
    week_start_date = datetime.datetime.now().strftime('%Y-%m-%d')
    for category, count in metrics['categories'].items():
        cursor.execute("INSERT INTO historical_metrics (week_start_date, project_id, version_id, type, name, count) VALUES (?, ?, ?, ?, ?, ?)",
                       (week_start_date, project_id, version_id, 'category', category, count))
    for severity, count in metrics['severities'].items():
        cursor.execute("INSERT INTO historical_metrics (week_start_date, project_id, version_id, type, name, count) VALUES (?, ?, ?, ?, ?, ?)",
                     (week_start_date, project_id, version_id, ‘severity’, severity, count))
for file_path, count in metrics[‘files’].items():
cursor.execute(“INSERT INTO historical_metrics (week_start_date, project_id, version_id, type, name, count) VALUES (?, ?, ?, ?, ?, ?)”,
(week_start_date, project_id, version_id, ‘file’, file_path, count))
cursor.execute(“INSERT INTO historical_metrics (week_start_date, project_id, version_id, type, name, count) VALUES (?, ?, ?, ?, ?, ?)”,
(week_start_date, project_id, version_id, ‘total’, ‘total_vulnerabilities’, metrics[‘total_vulnerabilities’]))
for status, count in metrics[‘audit_status’].items():
cursor.execute(“INSERT INTO historical_metrics (week_start_date, project_id, version_id, type, name, count) VALUES (?, ?, ?, ?, ?, ?)”,
(week_start_date, project_id, version_id, ‘audit_status’, status, count))
conn.commit()
conn.close()

if name == “main”:
main() 