from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    return render_template('gbp_usd_eur.html' )

    return "Hello, World!"
