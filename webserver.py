import http.server
import webbrowser
import os

# Set the path to the "frontend" directory in your script folder
frontend_dir = os.path.join(os.path.dirname(__file__), "frontend")
# Change to the "frontend" directory
os.chdir(frontend_dir)
# Create a simple HTTP server to serve the "frontend" directory
server_address = ('', 8080)
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
# Open the login page in the default web browser
login_page_url = 'http://localhost:8080/login/index.html'
webbrowser.open(login_page_url)

# Start the HTTP server
print(f"Serving at {login_page_url}. Press Ctrl+C to stop.")
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\nServer stopped.")