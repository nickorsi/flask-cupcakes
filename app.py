"""Flask app for Cupcakes"""

import os

from flask import Flask, request, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db


app = Flask(__name__)

app.config['SECRET_KEY'] = 'i-have-a-secret'

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.debug = True #---> Switch for debug toolbar, False=off True=on
toolbar = DebugToolbarExtension(app)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    "DATABASE_URL", "postgresql:///cupcakes")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True #---> When using SQL Alchemy

connect_db(app)
