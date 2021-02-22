from flask import Flask, render_template, session, request, redirect, url_for
from forms import ContactForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my-key'

@app.route("/")
def index():
    form = ContactForm()
    return render_template("home.html",form=form)

@app.route("/talks")
def talks():
    return render_template("talks.html")


if __name__ == "__main__":
    app.run(debug=True)
