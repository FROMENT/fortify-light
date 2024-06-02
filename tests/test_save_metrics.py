import unittest
import os
import sqlite3
from scripts.save_metrics import save_metrics_to_db

class TestSaveMetrics(unittest.TestCase):

    def setUp(self):
        self.db_path = 'data/vulnerabilities.db'
        if os.path.exists(self.db_path):
            os.remove(self.db_path)
        initialize_database()

    def test_save_metrics_to_db(self):
        metrics = {
            'categories': {'Category1': 1},
            'severities': {'High': 1},
            'files': {'file1': 1},
            'audit_status': {'audited': 1, 'unaudited': 0, 'false_positives': 0},
            'total_vulnerabilities': 1
        }
        project_id = 1
        version_id = 1
        save_metrics_to_db(metrics, project_id, version_id)

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM metrics")
        rows = cursor.fetchall()
        conn.close()

        self.assertGreater(len(rows), 0)

if __name__ == '__main__':
    unittest.main()