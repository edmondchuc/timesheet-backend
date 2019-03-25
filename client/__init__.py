def create(conn, user_id, name):
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO client VALUES(?, ?, ?)""", [None, user_id, name])
    conn.commit()
    return cursor.lastrowid


def get_one(conn, client_id):
    cursor = conn.cursor()
    rows = cursor.execute("""select s.duration, s.id from session as s
                      where s.client_id = ?""", [client_id])

    sessions = []
    for row in rows:
        sessions.append({'session_id': row['id'], 'duration': row['duration']})

    return sessions


def get_all(conn, user_id):
    cursor = conn.cursor()
    rows = cursor.execute("""select distinct s.client_id, c.name from client as c
                        join session as s on s.client_id = c.id
                        where user_id = ?""", [user_id])

    clients = []
    for row in rows:
        clients.append({'client_id': row['client_id'], 'name': row['name']})

    for client in clients:
        sessions = cursor.execute("""select s.duration, s.id from client as c
                                            join session as s on s.client_id = c.id
                                            where client_id = ?""", [client['client_id']])
        durations = []
        for session in sessions:
            durations.append({'session_id': session['id'], 'duration': session['duration']})
        client['row'] = durations

    return clients
