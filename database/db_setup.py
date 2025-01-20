import sqlite3
import random
from datetime import datetime

# Create database and table
conn = sqlite3.connect('project.db')
cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS weight_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    weight INTEGER,
    voltage1 REAL,
    voltage2 REAL,
    voltage3 REAL,
    voltage4 REAL,
    voltage5 REAL,
    voltage6 REAL,
    voltage7 REAL,
    voltage8 REAL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
""")

# Insert some test data
test_data = [
    (random.randint(100, 500),  # Random weight between 100-500
     random.uniform(1, 5),      # Random voltage between 1-5V
     random.uniform(1, 5),
     random.uniform(1, 5),
     random.uniform(1, 5),
     random.uniform(1, 5),
     random.uniform(1, 5),
     random.uniform(1, 5),
     random.uniform(1, 5),
     datetime.now())
    for _ in range(5)  # Create 5 test records
]

cursor.executemany("""
INSERT INTO weight_logs (weight, voltage1, voltage2, voltage3, voltage4, voltage5, voltage6, voltage7, voltage8, timestamp)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
""", test_data)

conn.commit()
conn.close()

print("Database setup complete with test data!")
