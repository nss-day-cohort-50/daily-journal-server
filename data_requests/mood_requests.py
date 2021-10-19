import json
import sqlite3

from data_requests.entry_requests import DB_PATH


def get_all_moods():
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute('select * from mood')

        dataset = db_cursor.fetchall()
        moods = []
        for row in dataset:
            mood = {
                'id': row['id'],
                'label': row['label'],
            }
            moods.append(mood)
        return json.dumps(moods)
