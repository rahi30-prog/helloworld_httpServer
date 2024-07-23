import unittest
import subprocess #Used to spawn new processes
import time
import requests #Used to send HTTP requests.

PORT = 8000 #Defines a port number.

class TestSimpleHTTPServer(unittest.TestCase):  #TestSimpleHTTPServer contain tests for the HTTP server.

    @classmethod    #Used to define a method that operates on the class directly.
    def setUpClass(cls):
        cls.server_process = subprocess.Popen(
            ['python', '-m', 'http.server', str(PORT)], #command to start the HTTP server 
        )

        time.sleep(1)   #Pauses execution for 1 second to allow the server to fully start before running any tests.

    @classmethod
    def tearDownClass(cls): #clean up resources after the tests are complete.
        cls.server_process.terminate()  #Sends a termination signal to the HTTP server process to stop it.

    def test_get_request(self):
        response = requests.get(f"http://localhost:{PORT}") #Sends a GET request to the server using the requests library and stores the response.
        self.assertEqual(response.status_code, 200)
        self.assertIn('text/html', response.headers['Content-Type'])    
        self.assertGreater(len(response.content), 0)    #Asserts that the response content length is greater than 0.

if __name__ == "__main__":
    unittest.main()
