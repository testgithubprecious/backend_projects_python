# router.py

ROUTES = {}

def route(path):
	def decorator(func):
		ROUTES[path] = func
		return func
	return decorator
