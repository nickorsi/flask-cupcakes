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
    # TODO: Could combine the below into one line
    cupcakes = Cupcake.query.all()
    serialized = [cupcake.serialize() for cupcake in cupcakes]

    return jsonify(cupcakes=serialized)

@app.get("/api/cupcakes/<int:cupcake_id>")
def get_cupcake(cupcake_id):
    """
    Returns data about a cupcakes or raise a 404 error if cupcake not found

    Returns JSON:{cupcakes: {id, flavor, size, rating, image_url}}.
    """
    # TODO: Could combine the below into one line
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
    # TODO: Could make request.jsnn a variable to make it easier to read
    flavor = request.json["flavor"]
    size = request.json["size"]
    rating = request.json["rating"]
    #Whats the best way to import default_image
    # TODO: Make reque.json['image_url'] or None
    # image_url = request.json.get("image_url", DEFAULT_IMAGE_URL)
    image_url = request.json["image_url"] or None
    # TODO: Combine lines 61 to 69 in one, define the variable below with request.json
    new_cupcake = Cupcake(
        flavor=flavor,
        size=size,
        rating=rating,
        image_url=image_url
    )

    db.session.add(new_cupcake)
    db.session.commit()

    # TODO: Could combine the 79 and 82 into one line
    serialized = new_cupcake.serialize()

    return (jsonify(cupcake=serialized), 201)

@app.patch("/api/cupcakes/<int:cupcake_id>")
def update_cupcake(cupcake_id):
    """
    Returns updated data about the cupcake or raise a 404 error if cupcake not found

    Returns JSON:{cupcake: {id, flavor, size, rating, image_url}}.
    """

    cupcake = Cupcake.query.get_or_404(cupcake_id)


    cupcake.flavor=request.json.get("flavor", cupcake.flavor)
    cupcake.size=request.json.get("size", cupcake.size)
    cupcake.rating=request.json.get("rating", cupcake.rating)
    cupcake.image_url=request.json.get("image_url" or cupcake.image_url)

    db.session.commit()

    return jsonify(cupcake=cupcake.serialize())

@app.delete("/api/cupcakes/<int:cupcake_id>")
def delete_cupcake(cupcake_id):
    """
    Deletes the specific cupcake instance with the ID matching the one in the URL
    or return 404 error if not found.

    Returns JSON: {deleted: [cupcake-id]}
    """

    cupcake = Cupcake.query.get_or_404(cupcake_id)

    db.session.delete(cupcake)
    db.session.commit()

    return jsonify(deleted=cupcake_id)