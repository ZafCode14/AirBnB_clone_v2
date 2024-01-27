"""Module with a flask script"""
#!/usr/bin/python3
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Method that closes storage"""
    storage.close()

@app.route("/states", strict_slashes=False)
def states():
    """Method that returns a template"""
    states = storage.all(State).values()
    return render_template('9-states.html', states=states, found=True)

@app.route("/states/<id>", strict_slashes=False)
def cities_by_states(id):
    """Method that returns a template"""
    found = False
    cities = True
    states = storage.all(State).values()
    for state in states:
        if state.id == id:
            found = True
            return render_template('9-states.html', state=state, cities=cities, found=found) 
    if not found:
        return render_template('9-states.html', found=found)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
