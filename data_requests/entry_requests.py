import json
import sqlite3
import datetime

DB_PATH = './daily-journal.db'


def get_all_entries():
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute('select * from entry')

        dataset = db_cursor.fetchall()
        entries = []
        for row in dataset:
            entry = {
                'id': row['id'],
                'concept': row['concept'],
                'entry': row['entry'],
                'moodId': row['moodId'],
                'data': row['date'],
                'tags': []
            }

            db_cursor.execute("""
            select t.id, t.label
            from entry e
            join EntryTag et on e.id = et.entry_id
            join Tag t on t.id = et.tag_id
            where e.id = ?
            """, (entry['id'],))

            tag_set = db_cursor.fetchall()
            for tag_data in tag_set:
                tag = {'id': tag_data['id'], 'label': tag_data['label']}
                entry['tags'].append(tag)
            entries.append(entry)
        return json.dumps(entries)


def get_single_entry(id):
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute('select * from entry where id = ?', (id, ))

        row = db_cursor.fetchone()

        entry = {
            'id': row['id'],
            'concept': row['concept'],
            'entry': row['entry'],
            'moodId': row['moodId'],
            'date': row['date']
        }
        return json.dumps(entry)


def delete_entry(id):
    with sqlite3.connect(DB_PATH) as conn:
        db_cursor = conn.cursor()
        db_cursor.execute('delete from entry where id = ?', (id, ))


def create_entry(new_entry):
    with sqlite3.connect(DB_PATH) as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Entry
            ( entry, concept, moodId, date )
        VALUES
            ( ?, ?, ?, ?);
        """, (new_entry['entry'], new_entry['concept'],
              new_entry['moodId'], datetime.datetime.now()))

        

        id = db_cursor.lastrowid

        new_entry['id'] = id

        for tag in new_entry['tags']:
            db_cursor.execute("""
                INSERT INTO EntryTag
                (entry_id, tag_id)
                values (?, ?)
            """, (id, tag))

        return json.dumps(new_entry)


def update_entry(id, updated_entry):
    with sqlite3.connect(DB_PATH) as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Entry
            SET
                entry = ?,
                concept = ?,
                moodId = ?,
                date = ?
        WHERE id = ?
        """, (updated_entry['entry'], updated_entry['concept'],
              updated_entry['moodId'], updated_entry['date'], id))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True
