from flask import render_template
from app import app
from BOFH import *
import random

x = random.randint(0,465)
response=bofh_text[x]

@app.route('/')
def index():
    return render_template('index.html', title='IT Help Desk', response=response)
