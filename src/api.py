from flask import Flask, request, jsonify
from flask_cors import CORS
from db import Database
from pixel import PixelEncoder

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
    pixels = Database("db/pixels.db").get_pixels()

    for pixel in pixels:
        dest.append(pixel)
    return(jsonify(dest))
