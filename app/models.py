from app import db
from datetime import datetime
from flask_user import UserMixin


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(255), server_default='')
    email_confirmed_at = db.Column(db.DateTime())
    picture = db.Column(db.String(255), nullable=False, server_default='default.jpg')
    thumbnail = db.Column(db.String(255), nullable=False, server_default='default-thumbnail.jpg')
    is_enabled = db.Column(db.Boolean(), nullable=False, default=False)
    first_name = db.Column(db.String(50), nullable=False, server_default='')
    last_name = db.Column(db.String(50), nullable=False, server_default='')
    description = db.Column(db.Text)
    roles = db.relationship('Role', secondary='user_roles')

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def is_active(self):
        return self.is_enabled

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Role(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)


class UserRoles(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('user.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('role.id', ondelete='CASCADE'))


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    body = db.Column(db.Text)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    last_modified = db.Column(db.DateTime)
    author = db.Column(db.Integer, db.ForeignKey('user.id', ondelete='CASCADE'))
    thumbnail = db.Column(db.String(255), nullable=False, server_default='cover-thumbnail.jpg')
    cover = db.Column(db.String(255), nullable=False, server_default='cover.jpg')
    album_id = db.Column(db.Integer(), db.ForeignKey('album.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.title)


class PostView(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    post_id = db.Column(db.Integer(), db.ForeignKey('post.id', ondelete='CASCADE'))


class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False, server_default='')
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    last_modified = db.Column(db.DateTime)

    def __repr__(self):
        return '<Post {}>'.format(self.title)


class Photos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(255), nullable=False, server_default='')
    album_id = db.Column(db.Integer(), db.ForeignKey('album.id', ondelete='CASCADE'))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<Post {}>'.format(self.path)

