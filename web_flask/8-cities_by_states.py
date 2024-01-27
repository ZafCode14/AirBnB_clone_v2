"""Module with a flask script"""
#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Method that closes storage"""
    storage.close()

@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states_list():
    """Method that returns a template"""
    states = storage.all(State).values()
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
