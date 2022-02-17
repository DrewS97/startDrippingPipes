# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client
from dotenv import load_dotenv

def sendMessage():
    load_dotenv()
    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
    auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                        body="It's going to be cold in the next 24 hours. Remember to drip your faucets!",
                        from_= os.environ.get('FROM'),
                        to='(217) 232-4238',
                    )

