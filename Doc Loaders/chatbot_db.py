import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect('chatbot_data.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS chat_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            role TEXT,
            message TEXT,
            timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_user(username):
    conn = sqlite3.connect('chatbot_data.db')
    c = conn.cursor()
    c.execute("INSERT OR IGNORE INTO users (username) VALUES (?)", (username,))
    conn.commit()
    conn.close()

def save_message(username, role, message):
    conn = sqlite3.connect('chatbot_data.db')
    c = conn.cursor()
    c.execute(
        "INSERT INTO chat_history (username, role, message, timestamp) VALUES (?, ?, ?, ?)",
        (username, role, message, datetime.now().isoformat())
    )
    conn.commit()
    conn.close()

def get_chat_history(username):
    conn = sqlite3.connect('chatbot_data.db')
    c = conn.cursor()
    c.execute(
        "SELECT role, message FROM chat_history WHERE username=? ORDER BY id ASC",
        (username,)
    )
    history = c.fetchall()
    conn.close()
    return history
