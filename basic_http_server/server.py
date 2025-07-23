#server.py

import socket
from router import ROUTES
import handlers #This will register the route

HOST = '127.0.0.1'
PORT = 8080

def handle_request(request):
	try:
		request_line = request.split("\r\n")
		parts = request_line.split(" ")
		if len(parts) < 3:
		    return "HTTP/1.1 400 Bad Request\r\n\r\nMalformed Request"

		method, path, _ = parts
		if method != "GET":
			return "HTTP/1.1 405 Method Not Allowed\r\n\r\nMethod Not Allowed"

		handler = ROUTES.get(path)
		if handler:
			body = handler()
			return f"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n{body}"
		else:
			return "HTTP/1.1 404 Not Found\r\n\r\nPage Not Found"
	except Exception as e:
		return f"HTTP/1.1 500 Internal Server Error\r\n\r\nError: {str(e)}"

def start_server():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		s.bind((HOST, PORT))
		s.listen()
		print(f"Server running at http://{HOST}:{PORT}")
		while True:
			conn, addr = s.accept()
			with conn:
				request = conn.recv(1024).decode()
				response = handle_request(request)
				conn.sendall(response.encode())

if __name__ == "__main__":
	start_server()

