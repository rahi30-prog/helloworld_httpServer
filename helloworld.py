from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):   #Get is used to retrieve the data.
        self.send_response(200) #Tells the user that the request is made
        self.send_header("Content-type", "text/plain")   #use it to specify the content type or length of the response.
        self.end_headers()  #Ends the header section(MUST be called after all headers have been sent, to complete the operation).
        self.wfile.write(b"Hello, World")   #b", because HTTP communication is done in bytes. wfile is used for writing a response back to the client

PORT = 8000 #Specifies port number

#Creates & starts an HTTP server
with HTTPServer(("", PORT), SimpleHandler) as server:   
    print("Server started at localhost:", PORT) #prints a startup message
    server.serve_forever()  #Keeps the server running.
