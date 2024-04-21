#!/usr/bin/python3
'''
Routes:
    /cities_by_states: display a HTML page: (inside the tag BODY)
    H1 tag: “States”
    UL tag: with the list of all State objects present in DBStorage
    sorted by name (A->Z) tip

    LI tag: description of one State: <state.id>: <B><state.name></B> + UL tag:
    with the list of City objects linked to the State sorted by name (A->Z)
    LI tag: description of one City: <city.id>: <B><city.name></B>
'''
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    '''display a HTML page with the list of all State-cities objects'''
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda x: x.name)

    # Load related cities for each state
    data = {}
    for state in sorted_states:
        cities = [city for city in state.cities]
        data[state.id] = sorted(cities, key=lambda city: city.name)

    return render_template('8-cities_by_states.html',
                           states=sorted_states, data=data)


@app.teardown_appcontext
def teardown_db(exception):
    '''Closes the db storage on teardown'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
