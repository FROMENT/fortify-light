import sqlite3
import datetime

def save_metrics_to_db(metrics, project_id, version_id):
    conn = sqlite3.connect('data/vulnerabilities.db')
    cursor = conn.cursor()

    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    for category, count in metrics['categories'].items():
        cursor.execute("INSERT INTO metrics (timestamp, project_id, version_id, type, name, count) VALUES (?, ?, ?, ?, ?, ?)",
                       (timestamp, project_id, version_id, 'category', category, count))

    for severity, count in metrics['severities'].items():
        cursor.execute("INSERT INTO metrics (timestamp, project_id, version_id, type, name, count) VALUES (?, ?, ?, ?, ?, ?)",
                       (timestamp, project_id, version_id, 'severity', severity, count))

    for file_path, count in metrics['files'].items():
        cursor.execute("INSERT INTO metrics (timestamp, project_id, version_id, type, name, count) VALUES (?, ?, ?, ?, ?, ?)",
                       (timestamp, project_id, version_id, 'file', file_path, count))

    cursor.execute("INSERT INTO metrics (timestamp, project_id, version_id, type, name, count) VALUES (?, ?, ?, ?, ?, ?)",
                   (timestamp, project_id, version_id, 'total', 'total_vulnerabilities', metrics['total_vulnerabilities']))

    for status, count in metrics['audit_status'].items():
        cursor.execute("INSERT INTO metrics (timestamp, project_id, version_id, type, name, count) VALUES (?, ?, ?, ?, ?, ?)",
                       (timestamp, project_id, version_id, 'audit_status', status, count))

    conn.commit()
    conn.close()