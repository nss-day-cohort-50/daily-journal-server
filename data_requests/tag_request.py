import json
import sqlite3

from data_requests.entry_requests import DB_PATH


def get_all_tags():
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute('select * from tag')

        dataset = db_cursor.fetchall()
        tags = []
        for row in dataset:
            tag = {
                'id': row['id'],
                'label': row['label'],
            }
            tags.append(tag)
        return json.dumps(tags)
