from flask import request, Flask
from twilio.twiml.messaging_response import MessagingResponse
from modules.sheet_auth import sheet
from modules.parse import get_contacts


app = Flask(__name__)


@app.route('/', methods=["POST"])
def bot_system():    
    
    user_msg = request.values.get('Body', '').lower()
    reply = False

    if user_msg == "contacts":
        contacts = get_contacts(sheet)
        reply = "\n".join([f"{first} {last}" for first, last in contacts]) 
    
    if reply is False:
        reply = "Sorry, we can't handle this."

    response = MessagingResponse()
    response.message(reply)

    return str(response)

if __name__ == "__main__":
    app.run()
