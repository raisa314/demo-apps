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

from model import Users, meetups
from model import db

app = Blueprint('main', __name__)

threads = []

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = Users.query.filter_by(email=email).first()
    # check if user actually exists
    # take the user supplied password, hash it, and compare it to the hashed password in database
    if not user or not check_password_hash(user.password, password): 
        flash('Please check your login details and try again.')
        return render_template('login.html') # if user doesn't exist or password is wrong, reload the page
   
    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    return render_template('index.html', meetups = meetups.query.all())

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def signup_post():

    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = Users.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again  
        flash('Email address already exists')
        return render_template('login.html')

    # create new user with the form data. Hash the password so plaintext version isn't saved.
    new_user = Users(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return render_template('login.html')

@app.route('/')
def index():
    return render_template('index.html', meetups = meetups.query.all())

@app.route('/meetup_all')
def meetup_all():
    my_dict = []
    my_dict_des = []
    my_dict_list = {}
    titles = [item.title for item in meetups.query.all()]
    for title_item in titles:
        my_dict.append(title_item)
    my_dict_list["Title"] = my_dict

    description = [item.description for item in meetups.query.all()]
    for des_item in description:
        my_dict_des.append(des_item)
    my_dict_list["description"] = my_dict_des

    with open("meetup_all.json", "w") as outfile:
     json.dump(my_dict_list, outfile)
    return my_dict_list

@app.route('/meetup_all/<int:id>')
def meetup_all_id(id):
    item_id_list = [item.title for item in meetups.query.filter_by(id=id)]
    des_id_list = [item.description for item in meetups.query.filter_by(id=id)]
    for item in item_id_list:
        print(item)
    for desItem in des_id_list:
        print(desItem)
    des = "Title:"+ " " + item + ", " + "Description:" + " "+ desItem
    return des

@app.route('/add_meetups')
def add_meetups():
    return render_template('add_meeting.html')

@app.route('/add_meetups', methods=['POST'])
def add_meetups_post():
    title = request.form.get('title')
    description = request.form.get('description')

    new_meeting = meetups(title = title, description = description)
    db.session.add(new_meeting)
    db.session.commit()
    return render_template('index.html', meetups = meetups.query.all())

@app.route('/meetup-details')
def meetup_details():
    titles = [item.title for item in meetups.query.all()]
    for item in titles:
        print(item)
    title = item
    description = [item.description for item in meetups.query.all()]
    for item in description:
        description = item
    return render_template('meetup-details.html', title = title, description = description)