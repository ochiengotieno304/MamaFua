from flask import Blueprint, request
from .models import User
from . import db

main = Blueprint('main', __name__)


@main.route('/voice', methods=['POST'])
def voice():
    session_id = request.values.get('sessionID', None)
    is_active = request.values.get('isActive', None)
    keypad_res = request.values.get('dtmfDigits', None)

    response = '<?xml version="1.0" encoding="UTF-8"?>'
    response += '<Response>'
    response += '<GetDigits finishOnKey="#">'
    response += '<Say>Hello, welcome to MamaFua, please enter an option followed by the hash sign</Say>'
    response += '</GetDigits>'
    response += '</Response>'

    if is_active == '1':
        if keypad_res == '1':
            response = '<?xml version="1.0" encoding="UTF-8"?>'
            response += '<Response>'
            response += '<Say>You selected option one</Say>'
            response += '</Response>'

    else:
        duration = request.values.get('durationInSeconds')
        currency_code = request.values.get('currencyCode')
        amount = request.values.get('amount')

    return response
