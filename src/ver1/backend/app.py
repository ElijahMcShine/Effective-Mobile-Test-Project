import http.server
import socketserver

PORT = 8080

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<html><head><title>Hello from Effective Mobile!</title></head>", "utf-8"))
            self.wfile.write(bytes("<body><p>Hello from Effective Mobile!</p>", "utf-8"))
            self.wfile.write(bytes("</body></html>", "utf-8"))
        else: self.send_response(404)


with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Сервер запущен на порту {PORT}")
    httpd.serve_forever()