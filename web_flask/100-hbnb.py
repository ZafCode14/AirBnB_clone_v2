#!/usr/bin/python3
"""Module with a flask script"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Method that closes storage"""
    storage.close()


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Method that returns a template"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()
    return render_template(
            '100-hbnb.html', states=states, amenities=amenities, places=places)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
