from eve.auth import BasicAuth
from flask import current_app as app
from flask import request as current_request

from core import Base
from core import Users
from core import Roles

from core import get_class_by_tablename

# this will be based on roles
# http://python-eve.org/authentication.html#role-based-access-control

class ChimasAuth(BasicAuth):

    def check_auth(self, login, password, allowed_roles, resource, method):

        try:
            lookup = list(current_request.view_args)[0]
        except IndexError:
            lookup = None

        #print("lookup: ",lookup,"\n", request.url, "\n", request.headers)

        user = Users.query.filter(Users.login == login).first()

        if 'anonymous' in allowed_roles and login == "anon":
            return True

        if user and user.password == password:
            is_authenticated = True

        if 'registered' in allowed_roles and is_authenticated:
            if is_authenticated:
                return True

        if 'owner' in allowed_roles and is_authenticated:
            res = get_class_by_tablename(resource)
            res_key = getattr(res,lookup.keys())
            restult = res.query.filter(res_key == lookup.values(), res.author_id == login)

            return True

        return False

        #else:
        #    return False
