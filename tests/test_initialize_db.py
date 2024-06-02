import unittest
import os
import sqlite3
from scripts.initialize_db import initialize_database

class TestInitializeDB(unittest.TestCase):

    def setUp(self):
        self.db_path = 'data/vulnerabilities.db'
        if os.path.exists(self.db_path):
            os.remove(self.db_path)

    def test_initialize_database(self):
        initialize_database()
        self.assertTrue(os.path.exists(self.db_path))

        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='metrics';")
        table_exists = cursor.fetchone()
        conn.close()

        self.assertIsNotNone(table_exists)

if __name__ == '__main__':
    unittest.main()