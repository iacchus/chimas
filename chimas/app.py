import cherrypy

cmx_conf = cherrypy.config.update({'server.socket_port': 41345})

USERNAME = "user1"
PASSWORD = "pass1"


class ChimasExtAuth:

    def __init__():
        self.exposed = True

    def validate_password(username,password):
        if username == USERNAME and password == PASSWORD:
            return True
        else:
            return False

class ChimasExtBBS:

    def __init__(self):
        pass

    @cherrypy.expose()
    def boards(self):
        return "This is boards().."

class Chimas(object):
    def __init__(self):
        self.initExtensions()
        #self.bbs = ChimasExtBBS()

    def initExtensions(self):
        self.bbs = ChimasExtBBS()


class App(object):
    def __init__(self):
        self.chimas = Chimas

    @cherrypy.expose
    def index(self):
        return "CHIMAS BBS SERVER, PLEASE USE A CLIENT."

if __name__ == '__main__':
    cherrypy.tree.mount(App().chimas(), '/', cmx_conf)

    cherrypy.engine.start()
    cherrypy.engine.block()
