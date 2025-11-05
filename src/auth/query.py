from src.database.execute import DBClient
from src.database.model import users, todo, subtodo

class TodoQueries:
    def __init__(self):
        self.db_client = DBClient()
    
    def get_todo(self):
        query = todo.select()
        rows = self.db_client.executeAll(query)
        return rows
    
    def insert_todo(self, todo_data):
        query = todo.insert().values(dict(todo_data)).returning(todo)
        rows = self.db_client.executeOne(query)
        return rows
    
    def update_todo(self, todo_data):
        query = todo.update().values(dict(todo_data)).returning(todo)
        rows = self.db_client.executeOne(query)
        return rows

    def get_subtodo(self):
        query = subtodo.select()
        rows = self.db_client.executeAll(query)
        return rows

    def insert_subtodo(self, subtodo_data):
        query = subtodo.insert().values(dict(subtodo_data)).returning(subtodo)
        rows = self.db_client.executeOne(query)
        return rows

    def update_subtodo(self, subtodo_data):
        query = subtodo.update().values(dict(subtodo_data)).returning(subtodo)
        rows = self.db_client.executeOne(query)
        return rows

    def get_user(self):
        query = user.select()
        rows = self.db_client.executeOne(query)
        return rows

    def insert_user(self, user_data):
        query = user.insert().values(dict(user_data)).returning(user)
        rows = self.db_client.executeOne(query)
        return rows

    


    
