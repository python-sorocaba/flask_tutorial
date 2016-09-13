import os
from random import choice

from flask import render_template, url_for, redirect, request

from tvseries import app, db
from tvseries.core.models import TVSerie
# ou ....
# from .models import TVSerie


@app.route('/')
def home(name=None):
    image_directory = os.path.join(app.static_folder, 'img')
    image_filenames = os.listdir(image_directory)
    image = os.path.join('img', choice(image_filenames))
    img_url = url_for('static', filename=image)
    series = TVSerie.query.all()
    return render_template('home.html', series=series, image=img_url)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form.to_dict().get('serie-name')
        description = request.form.to_dict().get('serie-description')
        author = request.form.to_dict().get('serie-author')
        episodies_number = request.form.to_dict().get('serie-episodes_number')

        serie = TVSerie(name=name, description=description, author=author,
                        episodies_number=episodies_number)
        db.session.add(serie)
        db.session.commit()
        return redirect('/')

    return render_template('add.html')
