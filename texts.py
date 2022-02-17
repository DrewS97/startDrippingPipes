import os, weather, ast
from twilio.rest import Client
from dotenv import load_dotenv

def sendMessage():
    load_dotenv()
    # Find your Account SID and Auth Token at twilio.com/console
    # and set the environment variables. See http://twil.io/secure
    account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
    auth_token = os.environ.get('TWILIO_AUTH_TOKEN')
    client = Client(account_sid, auth_token)
    
    low = weather.getLowestTemp()

    #Turn string representation of a dict into an actual dict
    phoneBook = ast.literal_eval(os.environ.get('PHONEBOOK'))

    for key in phoneBook:
        message = client.messages \
                        .create(
                            body=f"\nIt's going to be cold in the next 24 hours with the low being {low}F. Remember to drip your faucets!",
                            from_= os.environ.get('FROM'),
                            to= key,
                        )

