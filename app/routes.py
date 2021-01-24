from flask import render_template
from app import app
from BOFH import *
import random



@app.route('/')
def index():
    x = random.randint(0,465)
    response=bofh_text[x]
    return render_template('index.html', title='IT Help Desk', response=response)
