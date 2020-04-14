from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    id_astr = StringField('Id астронавта', validators=[DataRequired()])
    password_astr = PasswordField('Пароль астронавта', validators=[DataRequired()])
    id_cap = StringField('Id капитана', validators=[DataRequired()])
    password_cap = PasswordField('Пароль капитана', validators=[DataRequired()])
    submit = SubmitField('Доступ')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/<title>')
@app.route('/index/<title>')
def index(title):
    return render_template("ex1.html", title=title)


@app.route('/training/<prof>')
def training(prof):
    return render_template("ex2.html", prof=prof)


@app.route('/list_prof/<list_>')
def prof_list(list_):
    list_prof = ['инженер-исследователь', 'пилот', 'строитель', 'экзобиолог', 'врач',
                 'инженер по терраформированию', 'климатолог', 'специалист по радиационной защите',
                 'астрогеолог', 'гляциолог', 'инженер жизнеобеспечения', 'метеоролог',
                 'оператор марсохода', 'киберинженер', 'штурман', 'пилот дронов']
    return render_template("ex3.html", list_=list_, list_prof=list_prof)


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


@app.route('/login')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Доступ', form=form)


@app.route('/distribution')
def distribution():
    list_ = ['Ридл Скотт', 'Энди Уир', 'Марк Уотни', 'Венката Капур', 'Тедди Сандерс', 'Шон Бин']
    return render_template('distribution.html', title='Размещение', list_=list_)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
