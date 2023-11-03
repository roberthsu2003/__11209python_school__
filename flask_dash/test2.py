import dash
import dash_html_components as html
import flask
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.exceptions import NotFound
from werkzeug.serving import run_simple

from test2app1 import app1
from test2app2 import app2

server = flask.Flask(__name__)


@server.route("/")
def home():
    return "Hello, Flask2!"

application = DispatcherMiddleware(
    server,
    {"/app1": app1.server, "/app2": app2.server},
)

if __name__ == "__main__":
    run_simple("localhost", 8080, application,use_debugger=True,use_reloader=True)