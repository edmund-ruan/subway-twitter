import os
from twilio.rest import Client
import config

account_sid = config.TWILIO_ACCOUNT_SID
auth_token = config.TWILIO_AUTH_TOKEN

client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='This is the ship that made the Kessel Run in fourteen parsecs?',
         from_=config.TWILIO_PHONE_NUMBER, to=config.CELL_PHONE_NUMBER,
     )

print(message.sid)
