import random
import string

import cherrypy

cherrypy.config.update({'server.socket_port': 41345})

class App(object):
    @cherrypy.expose
    def index(self):
        return "CHIMAS BBS SERVER, PLEASE USE A CLIENT."

if __name__ == '__main__':
    cherrypy.quickstart(App())
