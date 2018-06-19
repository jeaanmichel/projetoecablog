from app import app
from datetime import datetime
from flask import render_template, flash, redirect
from app.models import User, Role, db
from flask_user import SQLAlchemyAdapter, UserManager, login_required, roles_required
from flask import Blueprint

editor = Blueprint('editor', __name__, url_prefix="/editor", template_folder='templates')
db_adapter = SQLAlchemyAdapter(db, User)
user_manager = UserManager(db_adapter, app)


# Cria os usuarios de teste
@app.before_first_request
def setup():
    # cria o usuario 'member@example.com' com role de editor
    if not User.query.filter(User.email == 'member@example.com').first():
        user = User(
            email='member@gmail.com',
            email_confirmed_at=datetime.now(),
            password=user_manager.hash_password('Password1'),
            username='member',
            first_name='First',
            last_name='Member',
            is_enabled=True
        )

        user.roles.append(Role(name='Editor'))
        db.session.add(user)
        db.session.commit()

    # cria o usuario 'admin@example.com' com roles 'admin'
    if not User.query.filter(User.email == 'admin@example.com').first():
        user = User(
            email='admin@example.com',
            email_confirmed_at=datetime.now(),
            password=user_manager.hash_password('Password1'),
            username='admin',
            first_name='Administrator',
            last_name='System',
            is_enabled=True
        )

        user.roles.append(Role(name='Admin'))
        db.session.add(user)
        db.session.commit()


@editor.route('/')
@login_required
@roles_required(['Editor'])
def index():
    return "You are on the editor homepage."
