from flask import Flask
import requests
import time
import smtplib
from email.message import EmailMessage
import hashlib
from urllib.request import urlopen
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    application.run()
