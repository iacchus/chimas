from eve import Eve

from eve_sqlalchemy import SQL
from eve_sqlalchemy.validation import ValidatorSQL

from core import Base as Base

from core import CommonTable
from core import Users, Boards, Posts

app = Eve(auth=None, validator=ValidatorSQL, data=SQL)

db = app.data.driver
Base.metadata.bind = db.engine
db.Model = Base
db.create_all()

methods_list = [ 'GET', 'HEAD', 'PATCH', 'POST', 'PUT', 'DELETE' ]
for each_method in methods_list:
    setattr(app, 'on_pre_{0}'.format(each_method), CommonTable.do_pre_method)
    setattr(app, 'on_post_{0}'.format(each_method), CommonTable.do_post_method)

if __name__ == "__main__":

#    app.on_pre_GET += CommonTable.do_method
#    app.on_pre_HEAD += CommonTable.do_method
#    app.on_pre_PATCH += CommonTable.do_method
#    app.on_pre_POST += CommonTable.do_method
#    app.on_pre_PUT += CommonTable.do_method
#    app.on_pre_DELETE += CommonTable.do_method

    app.run();
