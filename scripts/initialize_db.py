import sqlite3

def initialize_database():
    conn = sqlite3.connect('data/vulnerabilities.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS metrics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            project_id INTEGER,
            version_id INTEGER,
            type TEXT,
            name TEXT,
            count INTEGER
        )
    ''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS historical_metrics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            week_start_date TEXT,
            project_id INTEGER,
            version_id INTEGER,
            type TEXT,
            name TEXT,
            count INTEGER
        )
    ''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    initialize_database()
    print("Database initialized.")