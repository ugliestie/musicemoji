import sqlite3 as sq

db = sq.connect('./custom_covers.db')
cur = db.cursor()


async def db_start():
    cur.execute('''
                    CREATE TABLE IF NOT EXISTS custom_covers (
                        uri TEXT PRIMARY KEY,
                        file_id BOOLEAN
                    )
                ''')
    db.commit()
    
async def get_cover(uri):
    file_id = cur.execute('SELECT file_id FROM custom_covers WHERE uri = ?', (uri,)).fetchone()
    if file_id is None:
        return None
    return file_id[0]

async def write_cover(uri, file_id):
    cover = cur.execute("SELECT * FROM custom_covers WHERE uri = ?", (uri,)).fetchone()
    if not cover:
        cur.execute("INSERT INTO custom_covers VALUES (?, ?)", (uri, file_id))
    else:
        cur.execute("UPDATE INTO custom_covers SET file_id = ? WHERE uri = ?", (file_id, uri))
    db.commit()

async def delete_cover(file_id):
    cur.execute("DELETE FROM custom_covers WHERE file_id = ?", (file_id))
    db.commit()