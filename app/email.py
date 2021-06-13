from flask_mail import Message
from flask import render_template
from . import mail


def mail_message(subject,template,to,**kwargs):
    # stores our email addresses
    sender_email = "peterkiru560@gmail.com"
    # covers the subject sender email and recipients
    email = Message(subject, sender=sender_email, recipients=[to])
    # We then set up the email body and HTML. We use the send method of the mailinstance and pass in the email instance.
    email.body= render_template(template + ".txt",**kwargs)
    email.html = render_template(template + ".html",**kwargs)
    mail.send(email)