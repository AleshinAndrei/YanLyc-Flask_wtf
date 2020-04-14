from flask import Flask, render_template

app = Flask(__name__)


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template("ex1.html", title=title)


@app.route('/training/<prof>')
def training(prof):
    return render_template("ex2.html", prof=prof)


@app.route('/list_prof/<list_>')
def list_prof(list_):
    return render_template("ex3.html", list_=list_)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    params = {
        'title': 'Экспедиция на Марс!',
        'surname': 'Watny',
        'name': 'Mark',
        'education': 'выше среднего',
        'profession': 'штурман марсохода',
        'sex': 'male',
        'motivation': 'Всегда мечтал застрять на Марсе!',
        'ready': True
    }
    return render_template("auto_answer.html", **params)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')