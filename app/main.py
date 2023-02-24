import africastalking
from flask import Blueprint, request
from .models import User
from . import db

main = Blueprint('main', __name__)
location="Select location. For Lavington press 4. For kileleshwa press 5. For Westlands press 6"

username = "sandbox"    # use 'sandbox' for development in the test environment
api_key = "api_key"
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
            response += '<GetDigits finishOnKey="#">'
            response += '<Say>Select location. For Lavington press 4. For kileleshwa press 5. For Westlands press 6</Say>'
            response += '</GetDigits>'
            response += '</Response>'

        elif keypad_res == '2':
            response = '<?xml version="1.0" encoding="UTF-8"?>'
            response += '<Response>'
            response += '<GetDigits finishOnKey="#">'
            response += '<Say>Select location. For Lavington press 4. For kileleshwa press 5. For Westlands press 6</Say>'
            response += '</GetDigits>'
            response += '</Response>'

        elif keypad_res == '3':
            response = '<?xml version="1.0" encoding="UTF-8"?>'
            response += '<Response>'
            response += '<GetDigits finishOnKey="#">'
            response += '<Say>=Select location. For Lavington press 4. For kileleshwa press 5. For Westlands press 6</Say>'
            response += '</GetDigits>'
            response += '</Response>'

        elif keypad_res == '4':
            response = '<?xml version="1.0" encoding="UTF-8"?>'
            response += '<Response>'
            response += '<GetDigits finishOnKey="#">'
            response += '<Say>Select option 7 for morning or 8 for evening</Say>'
            response += '</GetDigits>'
            response += '</Response>'
            sms.send("Successfully booked cleaning session", ["+254790143657"])
        elif keypad_res == '5':
            response = '<?xml version="1.0" encoding="UTF-8"?>'
            response += '<Response>'
            response += '<GetDigits finishOnKey="#">'
            response += '<Say>Select option 7 for morning or 8 for evening</Say>'
            response += '</GetDigits>'
            response += '</Response>'
            sms.send("Successfully booked cleaning session", ["+254790143657"])
        elif keypad_res == '6':
            response = '<?xml version="1.0" encoding="UTF-8"?>'
            response += '<Response>'
            response += '<GetDigits finishOnKey="#">'
            response += '<Say>Select option 7 for morning or 8 for evening</Say>'
            response += '</GetDigits>'
            response += '</Response>'
            sms.send("Successfully booked cleaning session", ["+254790143657"])
        elif keypad_res == '7':
            response = '<?xml version="1.0" encoding="UTF-8"?>'
            response += '<Response>'
            response += '<Say>You have been booked for a morning appointment,we will send an sms confirmation</Say>'
            response += '</Response>'
            sms.send("Successfully booked cleaning session", ["+254790143657"])
        elif keypad_res == '8':
            response = '<?xml version="1.0" encoding="UTF-8"?>'
            response += '<Response>'
            response += '<Say>You have been booked for an evening appointment, we will send an sms confirmation</Say>'
            response += '</Response>'
            sms.send("Successfully booked cleaning session", ["+254790143657"])    

    else:
        duration = request.values.get('durationInSeconds')
        currency_code = request.values.get('currencyCode')
        amount = request.values.get('amount')

    return response
