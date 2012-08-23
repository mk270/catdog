
from catdog import db

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

