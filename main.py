# Download the helper library from https://www.twilio.com/docs/python/install
import os, weather
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
client = Client(account_sid, auth_token)


message = client.messages \
                .create(
                     body="Start Dripping",
                     from_='(309)322-9745',
                     to='+12172324238'
                 )

print(message.sid)
