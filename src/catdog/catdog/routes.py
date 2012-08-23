import pystache

from catdog import app
from models import *


def render(data):
    template = file('static/index.html').read()
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

@app.route('/recipients/<camp_id>')
def recipient_list(camp_id):
    return render({
            "recipient_list": True,
            "campaign": campaigns(),
            "recipient": recipients(camp_id)
            })

@app.route('/campaign/<camp_id>')
def campaign_detail(camp_id):
    return render({
            "campaign_detail": True,
            "name": Campaign.query.filter(Campaign.campaign_id==camp_id).first().camp_name,
            "camp_id": camp_id,
            "campaign": campaigns()
            })

@app.route('/send/<camp_id>', methods=['POST'])
def send_email(camp_id):
    return "Oops"

@app.route('/')
def hello_world():
    return render({ "home_page": True, "campaign": campaigns() })
