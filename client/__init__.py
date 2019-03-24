def create(conn, user_id, name):
    cursor = conn.cursor()
    cursor.execute("""INSERT INTO client VALUES(?, ?, ?)""", [None, user_id, name])
    conn.commit()
    return cursor.lastrowid


def get_all(conn, user_id):
    cursor = conn.cursor()
    rows = cursor.execute("""select distinct s.client_id, c.name from client as c
                        join session as s on s.client_id = c.id
                        where user_id = ?""", [user_id])

    clients = []
    for row in rows:
        clients.append({'client_id': row['client_id'], 'name': row['name']})

    for client in clients:
        sessions = cursor.execute("""select s.duration from client as c
                                            join session as s on s.client_id = c.id
                                            where client_id = ?""", [client['client_id']])
        durations = []
        for session in sessions:
            durations.append(session['duration'])
        client['row'] = durations

    return clients
