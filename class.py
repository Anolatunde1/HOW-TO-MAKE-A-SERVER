from http.server import HTTPServer, BaseHTTPRequestHandler

hostname = "localhost"
portnumber = 8090


class servername(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        global publish_this
        self.wfile.write(bytes(publish_this, "utf-8"))


if __name__ == "__main__":
    webserver = HTTPServer((hostname, portnumber), servername)
    print("YES, YOU HAVE THE WEBSERVER RUNNING AS http://%s:%s" %
          (hostname, portnumber))
    try:
        webserver.serve_forever()

    except KeyboardInterrupt:
        pass
    webserver.server_close()
    print("HEY LOOKS LIKE YOU STOPPED THE SERVER FROM RUNNING. ")
