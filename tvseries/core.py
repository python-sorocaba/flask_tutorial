from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/<name>')
def name(name):
    return render_template('home2.html', name=name)
