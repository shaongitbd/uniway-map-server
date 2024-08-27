import os.path
from flask import Flask, send_file
app = Flask(__name__, static_url_path='/static')
@app.route('/tiles/<zoom>/<y>/<x>', methods=['GET', 'POST'])
def tiles(zoom, y, x):
    default = 'tiles\\13\\6142\\3529.png' # this is a blank tile, change to whatever you want
    filename = '\tiles\\%s\\%s\\%s.png' % (zoom, x, y)
    if os.path.isfile(filename):
        return send_file(filename)
    else:
        return send_file(default)
@app.route('/', methods=['GET', 'POST'])
def index():
    return app.send_static_file('index.html')
