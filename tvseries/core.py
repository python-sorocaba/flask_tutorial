from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/<name>')
def home(name=None):
    return render_template('home.html', name=name)
