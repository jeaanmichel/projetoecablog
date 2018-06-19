from app import app
from flask import Blueprint

site = Blueprint('site', __name__)


@site.route('/')
def homepage():
    return 'You are on the site homepage'
