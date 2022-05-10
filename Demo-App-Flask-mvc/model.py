import psycopg2
import psycopg2.extras
#from psycopg2 import cursor
from flask import Flask, Blueprint, request, flash, url_for, redirect, render_template
from requests import post
from sqlalchemy import desc
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, LoginManager, login_user
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint
import json


controller = Flask(__name__)
#controller.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meetup.sqlite3'
controller.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:1234@localhost:5050/test'
controller.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(controller)

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(controller)

### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'controller_name': "Demo_controller_using_flask"
    }
)
controller.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
### end swagger specific ###


class meetups(db.Model):
   id = db.Column('meeting_id', db.Integer, primary_key=True)
   title = db.Column(db.String(100))
   description = db.Column(db.String(100))

class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))

def __init__(self, title, description):
   self.title = title
   self.description = description

@login_manager.user_loader
def load_user(id):
    # since the id is just the primary key of our user table, use it in the query for the user
    return Users.query.get(int(id))