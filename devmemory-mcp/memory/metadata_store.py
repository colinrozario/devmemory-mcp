import sqlite3
import uuid
from datetime import datetime

conn = sqlite3.connect("data/memory.db", check_same_thread=False)
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