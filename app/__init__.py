from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

from .editor import editor
from .site import site

# TODO - usar flask admin para a tela de admin
app.register_blueprint(site)
app.register_blueprint(editor)