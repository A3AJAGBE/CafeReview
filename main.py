import os

from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from dotenv import load_dotenv
load_dotenv()


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    submit = SubmitField('Submit')


app = Flask(__name__)
Bootstrap(app)
app.secret_key = os.environ.get('SECRET_KEY')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cafe')
def cafe():
    return render_template('cafe.html')


@app.route('/add', methods=('GET', 'POST'))
def add():
    form = CafeForm()
    if form.validate_on_submit():
        cafe_name = form.cafe.data
        with open('cafe-data.csv', mode='a') as csv_file:
            csv_file.write(f'{cafe_name}\n')
            return redirect(url_for('index'))
    return render_template('add.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
