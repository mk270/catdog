
# ok
# we don't stop running, now

# how to separate flask app into multiple files
# list of bits of the app
# html tabs for all the bits of the app
# mysoc lookup

# actions:
# display recipients
# tab scaffolding
# preview
# dispatch

import sqlite3
import pystache

from flask import Flask


from flask.ext.sqlalchemy import SQLAlchemy

DB = 'sqlite:///camp.db'
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///mk_blog'
db = SQLAlchemy(app)

#import models
from models import *

def get_campaigns():
    for cmp in Campaign.query.all():
        yield cmp.to_dict()

@app.route('/recipients/<camp_id>')
def recipients(camp_id):
    data = file('static/index.html').read()
    s = pystache.render(data, {
            "recipient":
             [ rcpt.person.to_dict() for rcpt in Recipient.query.filter(Recipient.campaign_id==camp_id) ]
            })
    return s

@app.route('/campaign/<camp_id>')
def campaign(camp_id):
    data = file('static/index.html').read()
    return "campid: %s" % camp_id

@app.route('/')
def hello_world():
    data = file('static/index.html').read()
    s = pystache.render(data, { "campaign": get_campaigns() })
    return s

def start():
    app.run(debug=True)

if __name__ == '__main__':
    start()
