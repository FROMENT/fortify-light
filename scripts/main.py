from fetch_data import fetch_projects, fetch_project_versions, fetch_updated_issues, fetch_issue_details, fetch_audit_history
from initialize_db import initialize_database
from extract_metrics import extract_metrics
from save_metrics import save_metrics_to_db, save_historical_metrics
from copy_metrics import copy_metrics_from_previous_week
import datetime
import sqlite3
import logging

# Configurer le journal de logs
logging.basicConfig(filename='fortify_light.log', level=logging.DEBUG, 
                    format='%(asctime)s %(levelname)s %(message)s')

def main():
    initialize_database()
    last_update_date = get_last_update_date()
    projects = fetch_projects()
    if projects is not None:
        for project in projects:
            project_id = project['id']
            project_name = project['name']
            project_updated = project['updated']
            if project_updated > last_update_date:
                update_project(project)
                versions = fetch_project_versions(project_id)
                if versions is not None:
                    for version in versions:
                        version_id = version['id']
                        version_name = version['name']
                        version_updated = version['updated']
                        if version_updated > last_update_date:
                            update_version(project_id, version)
                            issues = fetch_updated_issues(version_id, last_update_date)
                            if issues is not None and len(issues) > 0:
                                for issue in issues:
                                    issue_id = issue['issueId']
                                    issue_updated = issue['lastUpdateDate']
                                    if issue_updated > last_update_date:
                                        update_issue(version_id, issue)
                                        details = fetch_issue_details(issue_id)
                                        if details and details['lastUpdateDate'] > last_update_date:
                                            update_issue_details(issue_id, details)
                                        audits = fetch_audit_history(issue_id)
                                        for audit in audits:
                                            audit_updated = audit['lastUpdateDate']
                                            if audit_updated > last_update_date:
                                                update_audit(issue_id, audit)
                            else:
                                logging.info(f"No changes for version ID: {version_id}. Copying metrics from previous week.")
                                copy_metrics_from_previous_week(project_id, version_id)
                else:
                    logging.error(f"Failed to fetch versions for project ID: {project_id}")
    else:
        logging.error("Failed to fetch projects")

def get_last_update_date():
    conn = sqlite3.connect('data/vulnerabilities.db')
    cursor = conn.cursor()
    cursor.execute("SELECT MAX(updated_at) FROM vulnerabilities")
    result = cursor.fetchone()
    conn.close()
    if result and result[0]:
        return result[0]
    return '1970-01-01T00:00:00Z'

def update_project(project):
    conn = sqlite3.connect('data/vulnerabilities.db')
    cursor = conn.cursor()
    cursor.execute("""
        INSERT OR REPLACE INTO projects (id, name, description, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?)
    """, (project['id'], project['name'], project['description'], project['created'], project['updated']))
    conn.commit()
    conn.close()

def update_version(project_id, version):
    conn = sqlite3.connect('data/vulnerabilities.db')
    cursor = conn.cursor()
    cursor.execute("""
        INSERT OR REPLACE INTO project_versions (id, project_id, name, description, created_at, updated_at, start_date, due_date)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (version['id'], project_id, version['name'], version.get('description', ''), version['created'], version['updated'], version.get('startDate', ''), version.get('dueDate', '')))
    conn.commit()
    conn.close()

def update_issue(version_id, issue):
    conn = sqlite3.connect('data/vulnerabilities.db')
    cursor = conn.cursor()
    cursor.execute("""
        INSERT OR REPLACE INTO vulnerabilities (id, project_version_id, issue_name, status, audited, removed, found_date, last_update_date, first_detected_date, removed_date, primary_location, analysis_type, auditor_comment, reviewed, scan_status, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (issue['issueId'], version_id, issue['issueName'], issue['status'], issue['audited'], issue['removed'], issue['foundDate'], issue['lastUpdateDate'], issue.get('firstDetectedDate', ''), issue.get('removedDate', ''), issue.get('primaryLocation', ''), issue.get('analysisType', ''), issue.get('auditorComment', ''), issue.get('reviewed', ''), issue.get('scanStatus', ''), datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), issue['lastUpdateDate']))
    conn.commit()
    conn.close()

def update_issue_details(issue_id, details):
    conn = sqlite3.connect('data/vulnerabilities.db')
    cursor = conn.cursor()
    cursor.execute("""
        INSERT OR REPLACE INTO analysis_details (id, vulnerability_id, severity, category, recommendation, file_path, line_number, code_snippet, created_at, updated_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (details['issueId'], issue_id, details['severity'], details['category'],
details[‘recommendation’], details.get(‘file_path’, ‘’), details.get(‘line_number’, 0), details.get(‘code_snippet’, ‘’), datetime.datetime.now().strftime(’%Y-%m-%d %H:%M:%S’), details[‘lastUpdateDate’]))
conn.commit()
conn.close()

def update_audit(issue_id, audit):
conn = sqlite3.connect(‘data/vulnerabilities.db’)
cursor = conn.cursor()
cursor.execute(”””
INSERT OR REPLACE INTO audit_logs (id, vulnerability_id, action, timestamp, comment, created_at)
VALUES (?, ?, ?, ?, ?, ?)
“””, (audit[‘id’], issue_id, audit[‘action’], audit[‘date’], audit.get(‘comment’, ‘’), datetime.datetime.now().strftime(’%Y-%m-%d %H:%M:%S’)))
conn.commit()
conn.close()

if name == “main”:
main()
