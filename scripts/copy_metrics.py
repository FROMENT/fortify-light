import sqlite3
import datetime

def copy_metrics_from_previous_week(project_id, version_id):
    conn = sqlite3.connect('data/vulnerabilities.db')
    cursor = conn.cursor()

    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    last_week = (datetime.datetime.now() - datetime.timedelta(weeks=1)).strftime('%Y-%m-%d %H:%M:%S')

    cursor.execute('''
        INSERT INTO metrics (timestamp, project_id, version_id, type, name, count)
        SELECT ?, project_id, version_id, type, name, count
        FROM metrics
        WHERE timestamp = (SELECT MAX(timestamp) FROM metrics WHERE project_id = ? AND version_id = ?)
    ''', (timestamp, project_id, version_id))

    conn.commit()
    conn.close()