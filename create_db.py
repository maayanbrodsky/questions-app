from Models import Topics, Questions, Users
from Models import db


TABLES = [Topics, Questions, Users]

with db.connection_context():
    db.create_tables(TABLES, safe=True)
    db.commit()