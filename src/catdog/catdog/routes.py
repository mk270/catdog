import pystache

from catdog import app
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
