import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "AC5d33466a7084dd8e5d325a320f516f87"
auth_token = "868cfd6b2105a50b1ec7f6abf61da6f7"
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
         body='This is the ship that made the Kessel Run in fourteen parsecs?',
         from_='+13236414487',
         to='+16463615288'
     )

print(message.sid)
