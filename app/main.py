import africastalking
from flask import Blueprint, request
from .models import User
from . import db

main = Blueprint('main', __name__)


username = "sandbox"    # use 'sandbox' for development in the test environment
api_key = "key"
africastalking.initialize(username, api_key)


# Initialize a service e.g. SMS
sms = africastalking.SMS


@main.route('/voice', methods=['POST'])
def voice():
    session_id = request.values.get('sessionID', None)
    is_active = request.values.get('isActive', None)
    keypad_res = request.values.get('dtmfDigits', None)

    response = '<?xml version="1.0" encoding="UTF-8"?>'
    response += '<Response>'
    response += '<GetDigits finishOnKey="#">'
    response += '<Say>Hello, welcome to MamaFua, please enter an option followed by the hash sign'
    response += 'For laundry, press one. For house cleaning, press two. For utensils press three</Say>'
    response += '</GetDigits>'
    response += '</Response>'

    if is_active == '1':
        if keypad_res == '1':
            response = '<?xml version="1.0" encoding="UTF-8"?>'
            response += '<Response>'
            response += '<Say></Say>'
            response += '</Response>'

        elif keypad_res == '2':
            response = '<?xml version="1.0" encoding="UTF-8"?>'
            response += '<Response>'
            response += '<Say>You selected option two</Say>'
            response += '</Response>'

        elif keypad_res == '3':
            response = '<?xml version="1.0" encoding="UTF-8"?>'
            response += '<Response>'
            response += '<Say>You selected option three</Say>'
            response += '</Response>'

        elif keypad_res == '4':
            response = '<?xml version="1.0" encoding="UTF-8"?>'
            response += '<Response>'
            response += '<Say>You selected option four</Say>'
            response += '</Response>'
            sms.send("Successfully booked cleaning session", ["+254777287562"])


    else:
        duration = request.values.get('durationInSeconds')
        currency_code = request.values.get('currencyCode')
        amount = request.values.get('amount')

    return response
