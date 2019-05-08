"""Listener module."""
from sys import platform as _platform
from os import environ
import requests
import json
from telegram import ParseMode
from pync import Notifier
from flask import Flask, request
app = Flask(__name__)

# check for ngrok subdomain
ngrok = environ.get("NGROK_SUBDOMAIN", "")
BOT_URL = 'https://api.telegram.org/bot820797611:AAHv78eRIbvplSc-M5RvUvmCZryIE1_Fjzk/'


def display_intro():
    """Helper method to display introduction message."""
    if ngrok:
        message = "".join([
            "You can access this webhook publicly via at ",
            "http://%s.ngrok.io/webhook. \n" % ngrok,
            "You can access ngrok's web interface via http://localhost:4040"
        ])
    else:
        message = "Webhook server online! Go to http://localhost:5000"
    print (message)


def display_html(request):
    """
    Helper method to display message in HTML format.

    :param request: HTTP request from flask
    :type  request: werkzeug.local.LocalProxy
    :returns message in HTML format
    :rtype basestring
    """
    url_root = request.url_root
    if ngrok:
        return "".join([
            """Webhook server online! Go to """,
            """<a href="https://bitbucket.com">Bitbucket</a>""",
            """ to configure your repository webhook for """,
            """<a href="http://%s.ngrok.io/webhook">""" % ngrok,
            """http://%s.ngrok.io/webhook</a> <br />""" % ngrok,
            """You can access ngrok's web interface via """,
            """<a href="http://localhost:4040">http://localhost:4040</a>"""
        ])
    else:
        return "".join([
            """Webhook server online! """,
            """Go to <a href="https://bitbucket.com">Bitbucket</a>""",
            """ to configure your repository webhook for """,
            """<a href="%s/webhook">%s/webhook</a>""" % (url_root, url_root)
        ])


@app.route("/", methods=["POST"])
def index():
    """Endpoint for the root of the Flask app."""
    temp = json.dumps(request.get_json())
    extract = json.loads(temp)
    status = 'Successful deploy of *sellerlogin-gada*'

    message_notif = { 
        "chat_id": 721729890,
        "text": "♻️ (Notification) -- From " + extract['username'] +", "+ extract['text'] + "\n----------------------------------------------------------------------------\n" 
        + extract['attachments'][0]['title'] + "  ||  " + extract['attachments'][0]['footer'] + "\n"
        + extract['attachments'][0]['fallback'] + "\n"
    }

    if temp != status:
        message_url = BOT_URL + 'sendMessage'
        requests.post(message_url, json=message_notif)
    else:
        message_url = BOT_URL + 'sendMessage'
        requests.post(message_url, json=message_notif)
    # print(prepared_data)
    return display_html(request)

if __name__ == "__main__":
    display_intro()
    app.run(host="0.0.0.0", port=5000, debug=True)