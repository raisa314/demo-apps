import json
import logging

from flask import Flask, g, render_template
from flask_oidc import OpenIDConnect
import requests
import sqlite3
from flask_sqlalchemy import SQLAlchemy

logging.basicConfig(level=logging.DEBUG)

sqliteconnection = sqlite3.connect('meetup.sqlite3')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meetup.sqlite3'
app.config['SECRET_KEY'] = "random string"
db = SQLAlchemy(app)

app.config.update({
    'SECRET_KEY': 'yFzBz1nGR8VGMd3JfNbUOabEArduCTAI',
    'TESTING': True,
    'DEBUG': True,
    'OIDC_CLIENT_SECRETS': 'clients_secrets.json',
    'OIDC_ID_TOKEN_COOKIE_SECURE': False,
    'OIDC_REQUIRE_VERIFIED_EMAIL': False,
    'OIDC_USER_INFO_ENABLED': True,
    'OIDC_OPENID_REALM': 'flask-demo',
    'OIDC_SCOPES': ['openid', 'email', 'profile'],
    'OIDC_INTROSPECTION_AUTH_METHOD': 'client_secret_post'
})

class meetups(db.Model):
   id = db.Column('meeting_id', db.Integer, primary_key=True)
   title = db.Column(db.String(100))
   description = db.Column(db.String(100))

oidc = OpenIDConnect(app)

@app.route('/')
def hello_world():
    if oidc.user_loggedin:
        return ('Hello, %s, <a href="/private">See private</a> '
                '<a href="/logout">Log out</a>') % \
            oidc.user_getfield('preferred_username')
    else:
        return 'Welcome anonymous, <a href="/private">Log in</a>'


@app.route('/private')
@oidc.require_login
def hello_me():
    """Example for protected endpoint that extracts private information from the OpenID Connect id_token.
       Uses the accompanied access_token to access a backend service.
    """

    info = oidc.user_getinfo(['preferred_username', 'email', 'sub'])

    username = info.get('preferred_username')
    email = info.get('email')
    user_id = info.get('sub')

    if user_id in oidc.credentials_store:
        try:
            from oauth2client.client import OAuth2Credentials
            access_token = OAuth2Credentials.from_json(oidc.credentials_store[user_id]).access_token
            print ('access_token=<%s>') % access_token
            headers = {'Authorization': 'Bearer %s' % (access_token)}
            # YOLO
            greeting = requests.get('http://localhost:8080/greeting', headers=headers).text
        except:
            print ("Could not access greeting-service")
            greeting = "Hello %s" % username
    
    return render_template('index.html', meetups = meetups.query.all())


@app.route('/api', methods=['POST'])
@oidc.accept_token(require_token=True, scopes_required=['openid'])
def hello_api():
    """OAuth 2.0 protected API endpoint accessible via AccessToken"""

    return json.dumps({'hello': 'Welcome %s' % g.oidc_token_info['sub']})


@app.route('/logout')
def logout():
    """Performs local logout by removing the session cookie."""

    oidc.logout()
    return 'Hi, you have been logged out! <a href="/">Return</a>'


if __name__ == '__main__':
    app.run()