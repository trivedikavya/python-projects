import socket
import webbrowser
from http.server import SimpleHTTPRequestHandler
from socketserver import TCPServer

# Define host and port
HOST = '127.0.0.1'  # Localhost
PORT = 3000        # Port to serve the website

# Start the server
class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'index.html'  # Default to index.html
        return super().do_GET()

try:
    with TCPServer((HOST, PORT), CustomHandler) as httpd:
        print(f"Serving on http://{HOST}:{PORT}")

        # Automatically open the website in the default browser
        webbrowser.open(f"http://{HOST}:{PORT}")

        # Keep the server running
        httpd.serve_forever()
except OSError as e:
    print(f"Error: {e}")
