
from src.database.connection import engine


class DBClient:

    def executeAll(self, query):
        with engine.begin() as connection:
            rows = connection.execute(query).fetchall()
            return rows
        
    
    def executeOne(self, query):
        with engine.begin() as connection:
            rows = connection.execute(query).fetchone()
            return rows