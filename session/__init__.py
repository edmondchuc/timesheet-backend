def create(conn, client_id, session_date, duration):
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO session VALUES(?, ?, ?, ?)""", [None, client_id, session_date, duration])
    conn.commit()
    return cursor.lastrowid
