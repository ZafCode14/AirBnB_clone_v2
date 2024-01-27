"""Module with a falsk script"""
#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Module that closes storage"""
    storage.close()

@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Module that returns a template"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
