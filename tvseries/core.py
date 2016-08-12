import os
from random import choice

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
series = []


@app.route('/')
def home():
    names = os.listdir(os.path.join(app.static_folder, 'img'))
    img_url = url_for('static', filename=os.path.join('img', choice(names)))
    return render_template('home.html', series=series, image=img_url)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        serie_name = request.form.to_dict().get('serie-name')
        series.append(serie_name)
        return redirect('/')

    return render_template('add.html')
