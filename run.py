import os
import config
import datetime
import pandas as pd
from searchtweets import ResultStream, gen_rule_payload, load_credentials
from twilio.rest import Client


def twilio_connect():
    account_sid = config.TWILIO_ACCOUNT_SID
    auth_token = config.TWILIO_AUTH_TOKEN
    client_object = Client(account_sid, auth_token)
    return client_object


def send_message(client_name):
    return client_name.messages.create(from_=config.TWILIO_PHONE_NUMBER,
                                       to=config.CELL_PHONE_NUMBER,
                                       body="You don't have to move your car tonight. Enjoy your night!")


search_args = load_credentials(filename="secret.yaml",
                               yaml_key="search_tweets_api",
                               env_overwrite=True)
today = datetime.date.today()
print(today)

start_date = today + datetime.timedelta(-30)
print(start_date)

rule = gen_rule_payload("from:NYCASP",
                        from_date=str(start_date),
                        to_date=str(today),
                        results_per_call=50,
                        )
print(rule)

rs = ResultStream(rule_payload=rule,
                  max_results=50,
                  max_pages=1,
                  **search_args)
print(rs)

tweets = rs.stream()
list_tweets = list(tweets)
[print(tweet.all_text, end='\n\n') for tweet in list_tweets[0:5]]

tweet_text = []
tweet_date = []

for tweet in list_tweets:
    tweet_text.append(tweet['text'])
    tweet_date.append(tweet['created_at'])

df = pd.DataFrame({'tweet': tweet_text, 'date': tweet_date})
print(df.head())

df2 = pd.DataFrame({'tweet': ['suspend tomorrow'], 'date': [datetime.datetime(2021, 4, 2).strftime("%m %d %y")]})
print(df2.head())

client = twilio_connect()

if 'suspended' in df['tweet'].values[38]:
    if 'tomorrow' in df['tweet'].values[38]:
        send_message(client=client)
        print('text sent')
    else:
        print('suspended but not tomorrow, no text sent')
else:
    print('not suspended, no text sent')
