from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):   #Get is used to retrieve the data.
        self.send_response(200) #Tells the user that the request is made
        self.send_header("Content-type", "text/plain")  #Font
        self.end_headers()  #Ends the header section
        self.wfile.write(b"Hello, World")   #b", because HTTP communication is done in bytes

PORT = 8000 #Specifies port number

#Creates & starts an HTTP server
with HTTPServer(("", PORT), SimpleHandler) as server:   
    print("Server started at localhost:", PORT) #prints a startup message
    server.serve_forever()  #Keeps the server running.
