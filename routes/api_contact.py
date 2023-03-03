from flask import Flask, request
import smtplib
import ssl
import os

server = Flask(__name__)


def send_email(subject, sender_email, message):
    host = "smtp.gmail.com"
    port = 465

    username = "rabiighais@gmail.com"
    password = os.getenv("PASSWORD2")

    receiver = "rabiighais@gmail.com"
    context = ssl.create_default_context()

    body = f"Sender Email: {sender_email}\n\n{message}"
    message = f"Subject: {subject}\n\n{body}".encode('utf-8')

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
