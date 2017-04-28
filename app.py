import logging
import json
from flask import Flask
from flask_ask import Ask, question, statement


logging.getLogger('flask_ask').setLevel(logging.DEBUG)


app = Flask('__name__')
ask = Ask(app, '/')


@ask.launch
def launch():
    speech_text = "Contacts. What name do you want to look up?"
    help_text = "I didn't quite get that. You can ask, tell me about John Doe."
    return question(speech_text).reprompt(help_text)


@ask.intent('GetContact')
def get_contact(fname, lname):
    # load json file
    with open('sample_contacts.json') as data_file:
        contacts = json.load(data_file)

    speech_text = contacts[0]['description']
    # loop through contacts and find name
    # for contact in contacts:
    #     if contact['name'] == '{} {}'.format(fname.title(), lname.title()):
    #         speech_text = contact['description']
    #     else:
    #         speech_text = "Sorry I cannot find that contact."

    return statement(speech_text)


@ask.intent('AMAZON.CancelIntent')
def cancel():
    return statement("Goodbye")


@ask.intent('AMAZON.StopIntent')
def stop():
    return statement("Goodbye")


@ask.session_ended
def session_ended():
    return "", 200


if __name__ == '__main__':
    app.run(debug=True)
