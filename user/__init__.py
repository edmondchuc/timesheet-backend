from passlib.hash import pbkdf2_sha256


def create(conn, email, username, password_hash, date):
    cursor = conn.cursor()
    cursor.execute("""SELECT username FROM user WHERE username = ?""", [username])
    result = cursor.fetchone()

    if result is not None and result['username'] == username:
        return False

    cursor.execute("""INSERT INTO user VALUES (?, ?, ?, ?, ?)""",
                   [None, email, username, password_hash, date])
    conn.commit()
    return True


def login(conn, username, password):
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM user WHERE username = ?""",[username])
    result = cursor.fetchone()

    # Username did not match with anything in the database.
    if not result:
        return False

    # Password did not match with the password hash in the database.
    if not pbkdf2_sha256.verify(password, result['password_hash']):
        return False

    # Success, return the user's ID.
    return result['id']
