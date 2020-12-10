from Models import Topics, Questions, Users
from question_db import db


TABLES = [Topics, Questions, Users]

with db.connection_context():
    db.create_tables(TABLES, safe=True)
    db.commit()