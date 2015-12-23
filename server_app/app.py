import flask
from flask import Blueprint

from flask_socketio import SocketIO
from flask.ext.bcrypt import Bcrypt
from flask.ext.sqlalchemy import SQLAlchemy

from flask import Flask
app = Flask(__name__)
main = Blueprint('main', __name__)

# configuration
import config
app.config['SECRET_KEY'] = config.SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Chat.db'
app.config['PORT'] = config.port

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
socketio = SocketIO(app)

from controller import *