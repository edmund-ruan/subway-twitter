import os
from twilio.rest import Client

def twilio_connect():
    account_sid = config.TWILIO_ACCOUNT_SID
    auth_token = config.TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)
    return client

#python
def send_message(client):
    return client.messages.create(from_=config.TWILIO_PHONE_NUMBER,
    to=config.CELL_PHONE_NUMBER,
    body="You don't have to move your car tonight. Enjoy your night!")
