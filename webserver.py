import http.server
import webbrowser
import os

frontend_dir = os.path.join(os.path.dirname(__file__), "./frontend")
os.chdir(frontend_dir)
server_address = ('', 8080)
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
login_page_url = 'http://localhost:8080/login/index.html'
webbrowser.open(login_page_url)
print(f"Serving at {login_page_url}. Press Ctrl+C to stop.")
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\nServer stopped.")