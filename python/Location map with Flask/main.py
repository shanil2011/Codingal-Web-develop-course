from flask import Flask, jsonify, render_template, request
from geopy.geocoders import Nominatim

app = Flask(__name__)
geolocator = Nominatim(user_agent="location_me_app")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get_location", methods=["POST"])
def geocode():
    location = request.json.get("location")
    if not location:
        return jsonify({"error": "Location not founded"}), 400
    
    location = geolocator.geocode(location)
    if location:
        return jsonify({
            "address": location.address,
            "latitude": location.latitude,
            "longitude": location.longitude
        })
    else:
        return jsonify({"error": "Location not found"}), 404
    
if __name__ == "__main__":
    app.run(debug=True)