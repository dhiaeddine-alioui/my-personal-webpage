import logging

from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route('/')
@app.route('/fr')
def home_fr():
    return render_template('home_fr.html')

@app.route('/en')
def home_en():
    return render_template('home_en.html')


@app.errorhandler(500)
def server_error(e):
    # Log the error and stacktrace.
    logging.exception('An error occurred during a request.')
    return 'An internal error occurred.', 500
# [END app]
