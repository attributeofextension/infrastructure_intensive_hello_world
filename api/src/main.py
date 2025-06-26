import os
from http.server import HTTPServer, BaseHTTPRequestHandler
import sys


def create_handler(provider: str):
    class SimpleHandler(BaseHTTPRequestHandler):
        def __init__(self, *args, **kwargs):
            self.provider = provider
            super().__init__(*args, **kwargs)


        def do_GET(self):
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(f"Hello World (live from {self.provider})".encode())
    return SimpleHandler



def main():
    host = sys.argv[1] if len(sys.argv) > 1 else os.getenv('HOST','0.0.0.0')
    port = int(sys.argv[2]) if len(sys.argv) > 2 else int(os.getenv('PORT',8080))
    provider = os.getenv('PROVIDER','unknown')
    print(f"Server starting on {host}:{port}")

    server = HTTPServer((host, port), create_handler(provider))
    print(f"Server running on http://{host}:{port}")
    server.serve_forever()


if __name__ == "__main__":
    main()
