import os
from twilio.rest import Client

def twilio_connect():
    account_sid = "AC5d33466a7084dd8e5d325a320f516f87"
    auth_token = "868cfd6b2105a50b1ec7f6abf61da6f7"
    client = Client(account_sid, auth_token)
    return client

#python
def send_message(client):
    return client.messages.create(from_='+13236414487',
    to='+16463615288',
    body="You don't have to move your car tonight. Enjoy your night!")
