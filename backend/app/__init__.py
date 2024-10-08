from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_socketio import SocketIO
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
socketio = SocketIO(app, cors_allowed_origins="*")

from app import routes, socket_events

if __name__ == "__main__":
    socketio.run(app, debug=True)
