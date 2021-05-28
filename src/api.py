from flask import Flask, request, jsonify
from flask_cors import CORS
from db import Database
from pixel import PixelEncoder

DATABASE = "db/pixels.db"

# Instanciating Flask
app = Flask(__name__)

# Allowing api access from any ip
CORS(app)

# Enabling 
app.json_encoder = PixelEncoder

# Routes
@app.route("/api")
def hello_world():
    return "<a href='https://www.youtube.com/watch?v=dQw4w9WgXcQ'>Click for a surprise</a>"

@app.route("/api/pixels")
def list_all():
    dest = []
    pixels = Database(DATABASE).get_pixels()

    for pixel in pixels:
        dest.append(pixel)
    return(jsonify(dest))

@app.route("/api/pixels/<id>")
def get_specified(id):
    pixel = Database(DATABASE).get_pixel(id)

    if (pixel == None):
        return ("Not Found", 404)
    return ({"id": pixel.id, "color": pixel.color})

@app.route("/api/pixels/<id>/edit", methods = ["POST"])
def set_color(id):
    pixel = Database(DATABASE).get_pixel(id)
    color = request.args.get("color")
    #key = request.args.get("key")

    #if (pixel.key == key):
        #return ("Unauthorized : bad key", 401)
    if (not (len(color) == 6 and all(c in "0123456789abcdefABCDEF" for c in color))):
        return ("Invalid Color", 401)
    if (pixel == None):
        return ("Not Found", 404)
    if (Database(DATABASE).set_pixel(id, color)):
        return ("OK", 200)
    return ("Not Found", 404)
