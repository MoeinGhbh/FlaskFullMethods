import flask_sqlalchemy
from settings import app

db = flask_sqlalchemy.SQLAlchemy(app)


class Book(db.Model):
    __tableName__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    price = db.Column(db.Float, unique=True, nullable=False)
    isbn = db.Column(db.Integer)
