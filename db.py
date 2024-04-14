import sqlite3 as sq
import pytz
from datetime import datetime

async def db_start():
    global db, cur
    db = sq.connect('handlers/tg.db')
    cur = db.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS access_keys(
        key TEXT PRIMARY KEY
    )""")
    cur.execute("""
    CREATE TABLE IF NOT EXISTS authorized_users(
        user_id TEXT PRIMARY KEY
    )""")
    cur.execute("""
    CREATE TABLE IF NOT EXISTS tasks(
        task_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        task_text TEXT,
        difficulty INTEGER,
        status TEXT DEFAULT 'pending', -- pending, completed, canceled
        created_at TIMESTAMP DEFAULT (datetime('now', 'localtime')),
        completed_at TIMESTAMP
    )""")
    db.commit()

async def check_access(user_id: str) -> bool:
    cur.execute("SELECT 1 FROM authorized_users WHERE user_id = ?", (user_id,))
    return cur.fetchone() is not None

async def add_task(user_id: str, task_text: str, difficulty: int):
    # Замените 'localtime' на 'utc' для сохранения времени в UTC
    cur.execute("INSERT INTO tasks (user_id, task_text, difficulty, created_at) VALUES (?, ?, ?, datetime('now'))", (user_id, task_text, difficulty))
    db.commit()

# Добавьте здесь дополнительные функции по мере необходимости
# В db.py добавляем функцию для получения задач
async def get_tasks(user_id: str):
    cur.execute("SELECT task_id, task_text FROM tasks WHERE user_id = ? AND status = 'pending'", (user_id,))
    return cur.fetchall()

async def get_task_detail(task_id: int):
    cur.execute("SELECT task_text, difficulty, created_at, completed_at FROM tasks WHERE task_id = ?", (task_id,))
    task = cur.fetchone()
    if task:
        created_at = datetime.strptime(task[2], "%Y-%m-%d %H:%M:%S").replace(tzinfo=pytz.utc).astimezone(pytz.timezone('Europe/Moscow'))
        completed_at = datetime.strptime(task[3], "%Y-%m-%d %H:%M:%S").replace(tzinfo=pytz.utc).astimezone(pytz.timezone('Europe/Moscow')) if task[3] else None
        duration = completed_at - created_at if completed_at else None

        return {
            'task_text': task[0],
            'difficulty': task[1],
            'created_at': created_at.strftime("%d.%m.%Y %H:%M"),
            'completed_at': completed_at.strftime("%d.%m.%Y %H:%M") if completed_at else "Не завершено",
            'duration': str(duration)[:-3] if duration else "Не завершено"  # Обрезаем микросекунды
        }
    else:
        return None


#меняем значение выполнения задачи на true
async def mark_task_as_completed(task_id: int):
    # Аналогично, используйте UTC время при обновлении времени завершения задачи
    cur.execute("UPDATE tasks SET status = 'completed', completed_at = datetime('now') WHERE task_id = ?", (task_id,))
    db.commit()

#удаляем задание
async def delete_task(task_id: int):
    cur.execute("DELETE FROM tasks WHERE task_id = ?", (task_id,))
    db.commit()

#для клавиатуры чтобы получить все выполненные задачи
async def get_completed_tasks(user_id: str):
    cur.execute("SELECT task_id, task_text FROM tasks WHERE user_id = ? AND status = 'completed'", (user_id,))
    return cur.fetchall()
