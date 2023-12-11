"""Flask app for Cupcakes"""

import os

from flask import Flask, request, jsonify, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Cupcake, DEFAULT_IMAGE_URL


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

@app.get("/api/cupcakes")
def list_cupcakes():
    """
    Returns data about all cupcakes from each cupcake instance

    Returns JSON:{cupcakes: [{id, flavor, size, rating, image_url}, ...]}.
    """

    cupcakes = Cupcake.query.all()
    serialized = [cupcake.serialize() for cupcake in cupcakes]

    return jsonify(cupcakes=serialized)

@app.get("/api/cupcakes/<int:cupcake_id>")
def show_cupcake(cupcake_id):
    """
    Returns data about a cupcakes or raise a 404 error if cupcake not found

    Returns JSON:{cupcakes: {id, flavor, size, rating, image_url}}.
    """

    cupcake = Cupcake.query.get_or_404(cupcake_id)
    serialized = cupcake.serialize()

    return jsonify(cupcake=serialized)

@app.post("/api/cupcakes")
def create_cupcake():
    """
    Create a cupcake with flavor, size, rating, and image data from the body
    of  the request

    Returns JSON:{cupcakes: {id, flavor, size, rating, image_url}}.
    """

    flavor = request.json["flavor"]
    size = request.json["size"]
    rating = request.json["rating"]
    #Whats the best way to import default_image
    image_url = request.json.get("image_url", DEFAULT_IMAGE_URL)

    new_cupcake = Cupcake(flavor=flavor, size=size, rating=rating,
                           image_url=image_url)

    db.session.add(new_cupcake)
    db.session.commit()

    serialized = new_cupcake.serialize()

    return (jsonify(cupcake=serialized), 201)