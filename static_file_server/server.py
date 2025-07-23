import socket
import os
import mimetypes

HOST = 'localhost'
PORT = 8080
PUBLIC_DIR = './public'

def get_mime_type(file_path):
    mime_type, _ = mimetypes.guess_type(file_path)
    return mime_type or 'application/octet-stream'

def handle_request(request):
    try:
        request_line = request.splitlines()[0]
        method, path, _ = request_line.split()
        if method != 'GET':
            return b"HTTP/1.1 405 Method Not Allowed\r\n\r\n"

        if path == '/':
            path = '/index.html'

        file_path = os.path.join(PUBLIC_DIR, path.lstrip("/"))

        if not os.path.isfile(file_path):
            return b"HTTP/1.1 404 Not Found\r\n\r\nFile Not Found"

        with open(file_path, 'rb') as f:
            content = f.read()
            mime_type = get_mime_type(file_path)
            headers = (
                "HTTP/1.1 200 OK\r\n"
                f"Content-Type: {mime_type}\r\n"
                f"Content-Length: {len(content)}\r\n"
                "\r\n"
            )
            return headers.encode() + content

    except Exception as e:
        return b"HTTP/1.1 500 Internal Server Error\r\n\r\n" + str(e).encode()

def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"🌐 Static server running at http://{HOST}:{PORT}")

        while True:
            conn, addr = s.accept()
            with conn:
                request = conn.recv(1024).decode()
                response = handle_request(request)
                conn.sendall(response)

if __name__ == "__main__":
    start_server()

