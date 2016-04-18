import random
import string

import cherrypy

class StringGen(object):
    @cherrypy.expose
    def index(self):
        return "Hello wrld."

    @cherrypy.expose
    def generate(self):
        return ''.join(random.sample(string.hexdigits, 8))

if __name__ == '__main__':
    cherrypy.quickstart(StringGen())
