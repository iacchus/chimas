from eve.auth import BasicAuth
from flask import current_app as app

from core import Base
from core import Users

# this will be based on roles
# http://python-eve.org/authentication.html#role-based-access-control

class ChimasAuth(BasicAuth):

    def check_auth(self, login, password, allowed_roles, resource, method):

        print("login: {0}\npassword: {1}\n".format(login,password))
        user = app.data.driver.session.query(Users).get(login)

        if user and user.password == password:
            return True
        else:
            return False
