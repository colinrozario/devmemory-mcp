import sqlite3
import uuid
import os
from datetime import datetime

# Get absolute path to the data directory, creating it if it doesn't exist
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DB_DIR, exist_ok=True)
DB_PATH = os.path.join(DB_DIR, "memory.db")

conn = sqlite3.connect(DB_PATH, check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS memories (
id TEXT PRIMARY KEY,
type TEXT,
content TEXT,
file_path TEXT,
function_name TEXT,
importance INTEGER,
timestamp TEXT
)
""")

conn.commit()


def create_memory(type, content, file_path=None, function_name=None):

    memory_id = str(uuid.uuid4())

    cursor.execute("""
    INSERT INTO memories VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        memory_id,
        type,
        content,
        file_path,
        function_name,
        1,
        str(datetime.now())
    ))

    conn.commit()

    return memory_id