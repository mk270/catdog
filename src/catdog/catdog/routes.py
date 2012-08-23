import pystache

from catdog import app
from models import *

template = file('static/index.html').read()

def render(data):
    return pystache.render(template, data)

def campaigns():
    for cmp in Campaign.query.all():
        yield cmp.to_dict()

def recipients(camp_id):
    for rcpt in Recipient.query.filter(Recipient.campaign_id==camp_id):
        yield rcpt.person.to_dict()

@app.route('/campaign/new')
def new_campaign():
    return "placeholder for create new campaign"

@app.route('/campaign/<camp_id>')
def campaign_detail(camp_id):
    return render({
            "recipient_list": True,
            "campaign": campaigns(),
            "recipient": recipients(camp_id)
            })

@app.route('/')
def hello_world():
    return render({ "home_page": True, "campaign": campaigns() })
