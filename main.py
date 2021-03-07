import os

from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
Bootstrap(app)
app.secret_key = os.environ.get('SECRET_KEY')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/cafe')
def cafe():
    return render_template('cafe.html')


@app.route('/add')
def add():
    return render_template('add.html')


if __name__ == '__main__':
    app.run(debug=True)
