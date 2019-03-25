def create(conn, client_id, session_date, duration):
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO session VALUES(?, ?, ?, ?)""", [None, client_id, session_date, duration])
    conn.commit()
    return cursor.lastrowid


def update_one(conn, session_id, duration):
    cursor = conn.cursor()
    cursor.execute("""update session
                      set duration = ?
                      where session.id = ?""", [duration, session_id])

    conn.commit()
    return True
