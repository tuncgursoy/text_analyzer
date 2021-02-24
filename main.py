#!/usr/bin/env python3
# A web server to echo back a request's headers and data.
#
# Usage: ./webserver
#        ./webserver 0.0.0.0:5000

from http.server import HTTPServer, BaseHTTPRequestHandler
from sys import argv
import json
import cgi
import requests
import operation as op

BIND_HOST = 'localhost'
PORT = 8080
txt = {
    "text": "Deep pressure or deep touch pressure is a form of tactile sensory input. This input is most often delivered through firm holding, cuddling, hugging, firm stroking, and squeezing.\n\nHowever, before we get into too much detail about deep touch pressure, we need to understand our body’s sensory system and why deep touch pressure emerged in the first place.\n\nNeurologically, sensory processing is how we feel. Through processing sensory input, we make sense of the world around us. In everything we do, we are receiving sensory messages from both our bodies and the surrounding world."}
import urllib.parse as urlparse
from urllib.parse import parse_qs


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('content-type', 'application/json')
        self.end_headers()

    def do_POST(self):
        content_length = int(self.headers.get('content-length', 0))
        body = self.rfile.read(content_length)

        self.write_response(body)

    def do_GET(self):
        self._set_headers()
        self.wfile.write(json.dumps(txt).encode('utf-8'))
        url = self.path
        parsed = urlparse.urlparse(url)
        r = requests.get("http://localhost:8080/")


        try:
            print(parse_qs(parsed.query)['analysis'])
        except:
            print()

    # POST echoes the message adding a JSON field
    def do_POST(self):
        if self.path.endswith('/analyze'):
            ctype, pdict = cgi.parse_header(self.headers.getheader('content-type'))

            # refuse to receive non-json content
            if ctype != 'application/json':
                self.send_response(400)
                self.end_headers()
                return

    def write_response(self, content):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(content)

        print(self.headers)
        print(content.decode('utf-8'))


if len(argv) > 1:
    arg = argv[1].split(':')
    BIND_HOST = arg[0]
    PORT = int(arg[1])

if __name__ == '__main__':
    print(f'Listening on http://{BIND_HOST}:{PORT}\n')

    httpd = HTTPServer((BIND_HOST, PORT), SimpleHTTPRequestHandler)
    httpd.serve_forever()
