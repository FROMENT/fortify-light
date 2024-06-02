import unittest
import os
import sqlite3
from scripts.copy_metrics import copy_metrics_from_previous_week

class TestCopyMetrics(unittest.TestCase):

    def setUp(self):
        self.db_path = 'data/vulnerabilities.db'
        if os.path.exists(self.db_path):
            os.remove(self.db_path)
        initialize_database()
        # Insert sample data for copying
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO metrics (timestamp, project_id, version_id, type, name, count)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', ('2024-01-01T00:00:00Z', 1, 1, 'category', 'Category1', 10))
        conn.commit()
        conn.close()

    def test_copy_metrics_from_previous_week(self):
        project_id = 1
        version_id = 1
        copy_metrics_from_previous_week(project_id, version_id)

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM metrics WHERE timestamp = (SELECT MAX(timestamp) FROM metrics)")
        rows = cursor.fetchall()
        conn.close()

        self.assertGreater(len(rows), 1)

if __name__ == '__main__':
    unittest.main()