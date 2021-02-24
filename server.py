# Author Tunç Gürsoy 24/02/2021
# Define : Server Side of the TEXT ANALYZER challenge
# Example Routes :
# "http://localhost:8080/" Return the requests body
# "http://localhost:8080/analyze" Returns the full analysis of the given text
# "http://localhost:8080/analyze?analysis=<argument>,<argument>,.....   ===> Example : http://localhost:8080/analyze?analysis=wordCount,language   ||| http://localhost:8080/analyze?analysis=language  ||| etc...
# Arguments : wordCount, letters, longest, avgLength, duration, medianWordLength, medianWord, language

# Eng stop word list : https://gist.github.com/sebleier/554280
# TR stop word list : https://github.com/ahmetax/trstop

from http.server import BaseHTTPRequestHandler, HTTPServer
import json
class TempClass:
     parameter = []

txt = {
    "text": "Deep pressure or deep touch pressure is a form of tactile sensory input. This input is most often "
            "delivered through firm holding, cuddling, hugging, firm stroking, and squeezing.\n\nHowever, "
            "before we get into too much detail about deep touch pressure, we need to understand our body’s sensory "
            "system and why deep touch pressure emerged in the first place.\n\nNeurologically, sensory processing is "
            "how we feel. Through processing sensory input, we make sense of the world around us. In everything we "
            "do, we are receiving sensory messages from both our bodies and the surrounding world.",}

DEFAULT_PORT = 8080
LOCALHOST = '127.0.0.1'
DEFAULT_ENCODING = 'utf-16'
ROUTES = None
global parameter
import urllib.parse as urlparse
class Routes(object):
    def __init__(self):
        self.routes = self.__dict__
        global ROUTES
        ROUTES = self

    def add(self, route, cb):
        self.routes[route] = cb()

    def get(self, route):
        return self.routes.get(route)

    def exists(self, route):
        return route in self.routes

    def __call__(self, route):
        return self.get(route)


class Route(object):
    def __init__(self, route):
        self.route = route

    def __call__(self, func):
        ROUTES.add(self.route, func)


class RequestHandler(BaseHTTPRequestHandler):
    Routes()

    def send_msg(self, msg, encoding=DEFAULT_ENCODING):
        self.wfile.write(bytes(msg, encoding))

    def do_GET(self):

        if not ROUTES.exists(self.path) and self.path[0:8] !="/analyze":
            self.send_header('content-type', 'text/html')
            self.send_response(404)
            self.end_headers()
            self.send_msg('<center><h1>404 😩</h1></center>')
            return

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        if "analysis" in self.path:
            TempClass.parameter = urlparse.urlparse(self.path).query.split('=')[1].split(",")
            analysis = []
            import operation
            parameteres = []
            temp = operation.operation(txt["text"])
            try:
                analysis = txt["analysis"]
            except:
                pass
            for i in analysis:
                parameteres.append(i)
            for i in TempClass.parameter:
                parameteres.append(i)

            tempArr = {}
            if parameteres.__len__() != 0:
                    if "wordCount" in parameteres:
                        tempArr["wordCount"] = temp.calculateWordCount()
                    if "letters" in parameteres:
                        tempArr["letters"] = temp.letterCount()
                    if "longest" in parameteres:
                        tempArr["longest"] = temp.longest()
                    if "avgLength" in parameteres:
                        tempArr["avgLength"] = temp.avgLength()
                    if "duration" in parameteres:
                        tempArr["duration"] = temp.duration()
                    if "medianWordLength" in parameteres:
                        tempArr["medianWordLength"] = temp.med_word_count()
                    if "medianWord" in parameteres:
                        tempArr["medianWord"] = temp.med_word()
                    if "language" in parameteres:
                        tempArr["language"] = temp.detect_Language()
            self.send_msg(json.dumps(tempArr))
        else:
            TempClass.parameter = []
            self.send_msg(ROUTES(self.path))
        return


def run(port=8080, server_addr=LOCALHOST):
    print('starting server...')
    server_address = (server_addr, port)
    httpd = HTTPServer(server_address, RequestHandler)
    print('running server...')
    httpd.serve_forever()


if __name__ == '__main__':

    @Route('/')
    def root():
        return json.dumps(txt)
    @Route('/analyze')
    def analize():
        import operation
        temp = operation.operation(txt["text"])
        tempArr ={
    "wordCount": temp.calculateWordCount(),
    "letters": temp.letterCount(),
    "longest": temp.longest(),
    "avgLength": temp.avgLength(),
    "duration": temp.duration(),
    "medianWordLength": temp.med_word_count(),
    "medianWord": temp.med_word(),
    "language": temp.detect_Language()
         }
        return json.dumps(tempArr)

    run()
