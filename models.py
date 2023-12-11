"""Models for Cupcake app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE_URL = "https://tinyurl.com/demo-cupcake"

def connect_db(app):
    """Connect to the database."""
    app.app_context().push()
    db.app = app
    db.init_app(app)

class Cupcake(db.Model):
    """Cupcake"""

    __tablename__ = 'cupcakes'

    id = db.Column(
        db.Integer,
        autoincrement=True,
        primary_key=True,
    )

    flavor = db.Column(
        db.String(50),
        nullable=False,
    )

    size = db.Column(
        db.String(15),
        nullable=False,
    )

    rating = db.Column(
        db.Integer,
        nullable=False,
    )

    image_url = db.Column(
        db.String(500),
        nullable=False,
        default=DEFAULT_IMAGE_URL,
    )
