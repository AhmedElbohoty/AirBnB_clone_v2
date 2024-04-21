#!/usr/bin/python3
'''
Routes:
    /states: display a HTML page: (inside the tag BODY)
        H1 tag: “States”
        UL tag: with the list of all State objects present in DBStorage sorted
        by name (A->Z) tip
        LI tag: description of one State: <state.id>: <B><state.name></B>
    /states/<id>: display a HTML page: (inside the tag BODY)
        If a State object is found with this id:
        H1 tag: “State: ”
        H3 tag: “Cities:”
        UL tag: with the list of City objects linked to the State
        sorted by name (A->Z)
        LI tag: description of one City: <city.id>: <B><city.name></B>
    Otherwise:
        H1 tag: “Not found!”
'''
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def list_states_and_cities(state_id=None):
    '''List the states and cities sorted in alphabetical order'''
    states = storage.all(State)
    state = None

    if state_id:
        state = states.get(state_id)

    return render_template('9-states.html', states=states.values(),
                           state=state)


@app.teardown_appcontext
def teardown_db(exception):
    '''Closes the db storage on teardown'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
