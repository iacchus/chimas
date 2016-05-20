from eve import Eve

from eve_sqlalchemy import SQL
from eve_sqlalchemy.validation import ValidatorSQL

from core.auth import ChimasAuth
from core import Base as Base

from core import CommonTable
from core import Users, Boards, Posts

#app = Eve(auth=None, validator=ValidatorSQL, data=SQL)
app = Eve(auth=ChimasAuth, validator=ValidatorSQL, data=SQL)

#db = app.data.driver
#Base.metadata.bind = db.engine
#db.Model = Base
#db.create_all()

Base.metadata.bind = app.data.driver.engine
app.data.driver.Model = Base
app.data.driver.create_all()


methods_list = [ 'GET', 'HEAD', 'PATCH', 'POST', 'PUT', 'DELETE' ]
for each_method in methods_list:
    setattr(app, 'on_pre_{0}'.format(each_method), CommonTable.do_pre_method)
    setattr(app, 'on_post_{0}'.format(each_method), CommonTable.do_post_method)

if __name__ == "__main__":


    app.run();
