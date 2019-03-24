# API

| Route                                   | Action | HTTP Verb | Description                |
|-----------------------------------------|--------|-----------|----------------------------|
| `/user/create`                          | Create | POST      | Create a new user account. |
| `/user/login`                           | Read   | POST      | Authenticate a user.       |
| `/user/client`                          | Create | POST      | Create a new client.       |
| `/user/client/<client_id>`              | Read   | GET       | Get a list of all clients. |
| `/user/client/<client_id>`              | Update | PUT       | Update an existing client. |
| `/user/client/<client_id>`              | Delete | DELETE    | Delete an existing client. |
| `/user/client/<client_id>`              | Create | POST      | Create a new session.      |
| `/user/client/<client_id>/<session_id>` | Read   | GET       | Get a client's session.    |
| `/user/client/<client_id>/<session_id>` | Update | PUT       | Update a client's session. |
| `/user/client/<client_id>/<session_id>` | Delete | DELETE    | Delete a client's session. |