import json

# Pixel class
class Pixel:
    def __init__(self, db_pixel):
        id, color, key = db_pixel
        self.id = id
        self.color = color
        self.key = key
    
    def to_json(self):
        return {"filed": "ui"}

# JSON encoder
class PixelEncoder(json.JSONEncoder):
    def default(self, obj):
        if (isinstance(obj, Pixel)):
            return {"color": obj.color, "id": obj.id}
        return json.JSONEncoder.default(self, obj)