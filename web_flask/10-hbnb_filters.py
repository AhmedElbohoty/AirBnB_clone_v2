#!/usr/bin/python3
'''
Routes:
    /hbnb_filters: display a HTML page like 6-index.html, which was done
        during the project 0x01. AirBnB clone - Web static
        Copy files 3-footer.css, 3-header.css, 4-common.css and 6-filters.css
        from web_static/styles/ to the folder web_flask/static/styles
        Copy files icon.png and logo.png from web_static/images/ to the folder
        web_flask/static/images
        Update .popover class in 6-filters.css to allow scrolling in popover
        and a max height of 300 pixels.
'''
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """display a HTML page like 6-index.html from static"""
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    return render_template('10-hbnb_filters.html', states=states,
                           amenities=amenities)


@app.teardown_appcontext
def teardown_db(exception):
    '''Closes the db storage on teardown'''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5555')
