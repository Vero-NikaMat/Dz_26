
from flask import Flask, request, render_template
from functions import open_file

app = Flask(__name__)


@app.route('/')
def home_page():
    data = open_file('data/data.json')
    return render_template('index.html', data=data)
