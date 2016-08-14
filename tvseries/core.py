import os
from random import choice

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tvseries.sqlite3'
db = SQLAlchemy(app)
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


class TVSerie(db.Model):
    __table_args__ = {'sqlite_autoincrement': True}
    id = db.Column(db.BigInteger().with_variant(db.Integer, "sqlite"),
                   nullable=False, unique=True,
                   autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)
    episodies_number = db.Column(db.Integer, nullable=False, default=1)
    author = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        if self.description:
            self.description = "{0}...".format(self.description[0:10])

        return ("TVSerie(id={!r}, name={!r}, "
                "description={!r}, episodies_number={!r})").format(
            self.id, self.name,
            self.description,
            self.episodies_number)
