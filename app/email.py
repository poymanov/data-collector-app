from app import app, mail
from flask_mail import Message

def send_email(subject, recipients, text_body, html_body):
    msg = Message(subject, sender=app.config['MAIL_FROM'], recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    mail.send(msg)