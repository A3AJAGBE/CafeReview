import os
import csv
from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, url
from dotenv import load_dotenv
load_dotenv()


class CafeForm(FlaskForm):
    cafe = StringField('Cafe', validators=[DataRequired()])
    beverage = SelectField('Beverage', choices=['Tea 🫖', 'Coffee ☕', 'Chocolate 🧋️️'])
    location = StringField('Google Maps Location', validators=[DataRequired(), url()])
    rating = SelectField('Beverage Rating', choices=['★️', '★️★️️', '★️★️★️️', '★️★️★️★️', '★️★️★️★️★️️'])
    wifi = SelectField('Wifi Rating', choices=['👍🏼', '👍🏼👍🏼', '👍🏼👍🏼👍🏼', '👍🏼👍🏼👍🏼👍🏼', '👍🏼👍🏼👍🏼👍🏼👍🏼'])
    submit = SubmitField('Submit')


app = Flask(__name__)
Bootstrap(app)
app.secret_key = os.environ.get('SECRET_KEY')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cafe')
def cafe():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafe.html', cafes=list_of_rows)


@app.route('/add', methods=('GET', 'POST'))
def add():
    form = CafeForm()
    if form.validate_on_submit():
        cafe_name = form.cafe.data
        beverage = form.beverage.data
        location = form.location.data
        rating = form.rating.data
        wifi = form.wifi.data
        with open('cafe-data.csv', mode='a') as csv_file:
            csv_file.write(f'{cafe_name}, {beverage}, {location}, {rating}, {wifi}\n')
            return redirect(url_for('cafe'))
    return render_template('add.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
