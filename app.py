# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4

from flask import Flask
from gevent.wsgi import WSGIServer

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World'


if __name__ == '__main__':
    http_server = WSGIServer(('0.0.0.0', '5000'), app)
    http_server.serve_forever()
