from flask import Flask, render_template, request, redirect

app = Flask(__name__)
series = []


@app.route('/')
@app.route('/<name>')
def home(name=None):
    return render_template('home.html', name=name, series=series)


@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        serie_name = request.form.to_dict().get('serie-name')
        series.append(serie_name)
        return redirect('/')

    return render_template('add.html')
