from flask import Flask, render_template, session, request, redirect, url_for
from flask_mail import Mail, Message
from forms import ContactForm
import smtplib
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my-key'

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = ''
app.config['MAIL_PASSWORD'] = ''
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail = Mail(app)


@app.route("/", methods=["GET","POST"])
def index():
    form = ContactForm()
    if form.validate_on_submit():
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        notes = '''New message from coryjez.com. \n
                 From: {} \n
                 Message: {} \n
                 Return email: {} \n
                 Email automatically generated from coryjez.com
                 '''.format(name,message,email)
        msg = Message('New Message from CoryJez.com', sender = app.config['MAIL_USERNAME'], recipients =[app.config['MAIL_USERNAME']])
        msg.body = notes
        mail.send(msg)

        return render_template("home.html",form=form, sent=1, name=name)
    return render_template("home.html",form=form, sent=0)

@app.route("/talks")
def talks():
    return render_template("talks.html")


if __name__ == "__main__":
    app.run(debug=True)
