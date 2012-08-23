
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

class Campaign(db.Model):
    campaign_id = db.Column(db.Integer, primary_key=True)
    camp_name = db.Column(db.String(80), unique=True)
    template = db.Column(db.String(120))
    status = db.Column(db.String(10))
    predicate = db.Column(db.String(1000))

    def __init__(self, campaign_id, camp_name, template, status, predicate):
        self.campaign_id = campaign_id
        self.camp_name = camp_name
        self.template = template
        self.status = status
        self.predicate = predicate

    def __repr__(self):
        return '<Campaign %r>' % self.campaign_id

    def to_dict(self):
        return { "name": self.camp_name,
                 "camp_id": self.campaign_id }

class Person(db.Model):
    person_id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    postcode = db.Column(db.String(10))
    email_address = db.Column(db.String(100))
    
    def __init__(self, person_id, firstname, lastname, postcode, email_address):
        self.person_id = person_id
        self.firstname = firstname 
        self.lastname = lastname 
        self.postcode = postcode 
        self.email_address = email_address

    def __repr__(self):
        return '<Person %r>' % self.person_id

    def to_dict(self):
        return { "first_name": self.firstname,
                 "last_name": self.lastname, 
                 "email_address": self.email_address }

class Recipient(db.Model):
    __tablename__ = 'campaign_person'
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaign.campaign_id'), primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey('person.person_id'), primary_key=True)

    campaign = db.relationship("Campaign", backref=db.backref('campaign', order_by=campaign_id))
    person = db.relationship("Person", backref=db.backref('person', order_by=person_id))

    def __init__(self, campaign_id, person_id):
        self.campaign_id = campaign_id
        self.person_id = person_id

    def __repr__(self):
        return "<CampaignPerson>"

    def to_dict(self):
        return { "name": self.person.firstname }


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

if __name__ == '__main__':
    app.run(debug=True)
