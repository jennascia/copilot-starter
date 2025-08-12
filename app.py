
# Import necessary modules
from flask import Flask  # Flask is a lightweight web application framework
import time  # Provides time-related functions


# Create a Flask application instance
app = Flask(__name__)


def seconds_since_epoch():
    """
    Returns the number of seconds since the Unix epoch (January 1, 1970).
    """
    epoch = time.time()
    return int(epoch)


# Route for seconds since epoch
@app.route("/")
def seconds():
    """
    Returns the current time in seconds since the Unix epoch.
    """
    return str(seconds_since_epoch())


# Route for minutes since epoch
@app.route("/minutes")
def minutes():
    """
    Returns the current time in minutes since the Unix epoch.
    """
    return str(int(time.time() // 60))


# Route for hours since epoch
@app.route("/hours")
def hours():
    """
    Returns the current time in hours since the Unix epoch.
    """
    return str(seconds_since_epoch() // 3600)


# Route for days since epoch
@app.route("/days")
def days():
    """
    Returns the current time in days since the Unix epoch.
    """
    return str(seconds_since_epoch() // 86400)

