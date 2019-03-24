import logging
from flask import Flask, g
from config import Config
from controller import routes
import os
from flask_cors import CORS

app = Flask(__name__, template_folder=Config.TEMPLATES_DIR, static_folder=Config.STATIC_DIR)
app.register_blueprint(routes.routes)
app.secret_key = Config.FLASK_SECRET
CORS(app)


@app.before_first_request
def before_first_request():
    conn = routes.get_db()
    c = conn.cursor()
    with open(os.path.join(Config.APP_DIR, 'schema.sql')) as f:
        script = f.read()
    c.executescript(script)


if __name__ == '__main__':
    logging.basicConfig(filename=Config.LOGFILE,
                        level=logging.DEBUG,
                        datefmt='%Y-%m-%d %H:%M:%S',
                        format='%(asctime)s %(levelname)s %(filename)s:%(lineno)s %(message)s')

    app.run(debug=Config.DEBUG, threaded=True)
