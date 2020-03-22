from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from random import randint

# Creating intance of Flask class: the application
app = Flask(__name__)

# Allowing api access from any server
CORS(app)

# Configuring database connection
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///../../db/pixels.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Defining the db main table with a class
class Pixel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.String(6))
    key = db.Column(db.Integer)

    def __init__(self, color):
        self.color = color
        self.key = randint(0, 100000)

# Defining what URL should trigger a function
@app.route("/")
def hello_world():
    return ("<a href='https://www.youtube.com/watch?v=dQw4w9WgXcQ'>Click for a surprise</a>")

@app.route("/pixels")
def list_all():
    pixels = Pixel.query.all()
    dest = []

    for pixel in pixels:
        dest.insert(0, {"id": pixel.id, "color": pixel.color})
    return (jsonify(dest))

@app.route("/pixels/<id>")
def get_specified(id):
    pixel = Pixel.query.get(id)

    if (pixel != None):
        return ({"id": id, "color": pixel.color})
    else:
        return ("Not found", 404)

@app.route("/pixels/<id>/edit", methods = ['POST'])
def edit(id):
    pixel = Pixel.query.get(id)
    color = request.args.get('color')
    #key = request.args.get('key')

    #if (pixel.key == key):
        #return ("Unauthorized : bad key", 401)
    if (pixel != None):
        pixel.color = color
        pixel.key = randint(0, 100000)
        db.session.commit()
        return ({"id": pixel.id, "color": pixel.color})
    return ("Not found", 404)

