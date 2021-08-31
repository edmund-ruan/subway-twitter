import os
from twilio.rest import Client
import config

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
<<<<<<< HEAD
account_sid = ""
auth_token = ""
=======
account_sid = config.TWILIO_ACCOUNT_SID
auth_token = config.TWILIO_AUTH_TOKEN
>>>>>>> secondFeature
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='This is the ship that made the Kessel Run in fourteen parsecs?',
         from_=config.TWILIO_PHONE_NUMBER, to=config.CELL_PHONE_NUMBER,
     )

print(message.sid)
