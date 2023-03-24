import http.server
import socketserver

PORT = 8080

class VisitorCounter(http.server.SimpleHTTPRequestHandler):
    visitors = {}

    def do_GET(self):
        ip = self.client_address[0]
        if ip not in self.visitors:
            self.visitors[ip] = True
        self.send_response(200)
        self.end_headers()
        self.wfile.write("Você é o visitante de número: {}".format(len(self.visitors)).encode('utf-8'))

Handler = VisitorCounter

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Servindo na porta:", PORT)
    httpd.serve_forever()
