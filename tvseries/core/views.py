import os
from random import choice

from flask import render_template, url_for, redirect

from tvseries.ext import db
from tvseries.core import core_blueprint
from tvseries.core.models import TVSerie
from tvseries.core.forms import TVSerieForm


@core_blueprint.route('')
def home(name=None):
    image_directory = os.path.join(core_blueprint.static_folder, 'img')
    image_filenames = os.listdir(image_directory)
    image = os.path.join('img', choice(image_filenames))
    img_url = url_for('core.static', filename=image)
    series = TVSerie.query.all()
    return render_template('home.html', series=series, image=img_url)


@core_blueprint.route('add', methods=['GET', 'POST'])
def add():
    form = TVSerieForm()
    if form.validate_on_submit():
        name = form.name.data
        description = form.description.data
        author = form.author.data
        episodies_number = form.episodies_number.data
        year = form.year.data
        serie = TVSerie(name=name, description=description, author=author,
                        episodies_number=episodies_number, year=year)
        db.session.add(serie)
        db.session.commit()
        return redirect('/')

    return render_template('add.html', form=form)
