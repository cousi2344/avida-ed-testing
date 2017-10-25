import threading
import os

from shutil import copyfile

from http.server import SimpleHTTPRequestHandler, HTTPServer

from base.config import Configuration


class CustomWebServer:

    def __init__(self):
        """
        Initializes a CustomWebServer object.
        """
        self.config = Configuration()
        self.test_path = os.getcwd()
        self.chromedriver_path = "\chromedriver.exe"
        self.ui_path = self.config.get_ui_path()
        self.server_address = ('127.0.0.1', 8000)
        self.httpd = HTTPServer(self.server_address, SimpleHTTPRequestHandler)
        self.full_chromedriver_path = ""

    def run_http_server(self):
        """
        Creates a basic HTTP server so that the Avida-ED UI can be run locally.

        :return: None.
        """
        os.chdir(self.ui_path)
        os.chdir("..") # Move up one more directory
        self.full_chromedriver_path = os.getcwd() + self.chromedriver_path
        if not os.path.isfile(self.full_chromedriver_path):
            copyfile(self.test_path + self.chromedriver_path,
                 self.full_chromedriver_path)
        threading.Thread(target=self.httpd.serve_forever, daemon=True).start()

    def cleanup(self):
        """
        Cleans up after the server by changing back to the correct directory.

        :return: None.
        """
        os.chdir(self.test_path)
        self.httpd.server_close()
