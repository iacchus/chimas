from eve import Eve

from eve_sqlalchemy import SQL
from eve_sqlalchemy.validation import ValidatorSQL

from core import Base as Base

from core import Users, Boards, Posts

app = Eve(auth=None, validator=ValidatorSQL, data=SQL)

db = app.data.driver
Base.metadata.bind = db.engine
db.Model = Base
db.create_all()

if __name__ == "__main__":

    app.run();
