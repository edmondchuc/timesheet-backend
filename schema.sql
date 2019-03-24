create table if not exists user (
    id integer primary key autoincrement,
    email VARCHAR,
    username VARCHAR,
    password_hash VARCHAR,
    created_date date
);

create table if not exists client (
    id integer primary key autoincrement,
    user_id integer,
    name varchar,
    foreign key(user_id) references user(id)
);

create table if not exists session (
    id integer primary key autoincrement,
    client_id integer,
    session_date date,
    duration integer,
    foreign key(client_id) references client(id)
);