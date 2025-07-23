
# handlers.py
from router import route

@route("/")
def home():
	return "<h1>About Us</h1>"
