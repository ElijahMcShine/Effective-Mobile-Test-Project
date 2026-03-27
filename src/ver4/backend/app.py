import http.server
import socketserver
import psycopg2
import os
import random

PORT = 8080
POSTGRES_PASSWORD = os.environ['POSTGRES_PASSWORD']
POSTGRES_USER = os.environ['POSTGRES_USER']
POSTGRES_DB = os.environ['POSTGRES_DB']
POSTGRES_HOST = os.environ['POSTGRES_HOST']

class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<html><head><title>Hello from Effective Mobile!</title></head>", "utf-8"))
            cursor.execute("SELECT * FROM answers WHERE id = " + str(random.randint(1, 5)))
            answer = cursor.fetchall()
            self.wfile.write(bytes("<body><p>" + str(answer[0][1]) + "</p>", "utf-8"))
            self.wfile.write(bytes("</body></html>", "utf-8"))
            print("Host:" + str(self.headers.get_all("Host")) + " X-Real-IP:" + str(self.headers.get_all("X-Real-IP")) \
                  + " X-Forwarded-For:" + str(self.headers.get_all("X-Forwarded-For")) + " X-Forwarded-Proto:" + str(self.headers.get_all("X-Forwarded-Proto")))
        else: self.send_response(404)

if __name__ == '__main__':

    conn = psycopg2.connect(dbname=POSTGRES_DB, user=POSTGRES_USER, password=POSTGRES_PASSWORD, host=POSTGRES_HOST)
    cursor = conn.cursor()

    with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
        print(f"Сервер запущен на порту {PORT}")
        httpd.serve_forever()