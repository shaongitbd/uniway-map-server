import os.path
from flask import Flask, send_file
app = Flask(__name__, static_url_path='/static')
@app.route('/tiles/<zoom>/<x>/<y>', methods=['GET', 'POST'])
def tiles(zoom, x, y):
    default = 'tiles/14/12298/7064.png' # this is a blank tile, change to whatever you want
    filename = f'tiles/{zoom}/{x}/{y}'
    if os.path.isfile(filename):
       return send_file(filename)
    else:
       return send_file(default)
@app.route('/', methods=['GET', 'POST'])
def index():
    return app.send_static_file('index.html')
