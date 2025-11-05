
from src.database.model import users, todo, subtodo
from src.auth.query import TodoQueries
class TodoService:
    def __init__(self):
        self.todo_query = TodoQueries()

    def get_todos(self):
        rows = self.todo_query.get_todo()
        if not rows:
            raise
        return rows

    def insert_todos(self):
        rows = self.todo_query.insert_todo(sub_data)
        if not rows:
            raise
        return rows

    def update_todos(self):
        rows = self.todos_query.update_todos(sub_data)
        if not rows:
            raise
        return rows

    def get_subtodos(self):
        rows = self.subtodo_query.get_subtodo()
        if not rows:
            raise
        return rows

    def insert_subtodos(self, sub_data):
        rows = self.subtodo_query.insert_subtodo(sub_data)
        if not rows:
            raise
        return rows

    def update_subtodos(self):
        rows = self.subtodo_query.update_subtodo(sub_data)
        if not rows:
            raise
        return rows

     def get_user(self):
        rows = self.user_query.get_user()
        if not rows:
            raise
        return rows

    def insert_user(self):
        rows = self.user_query.insert_user(sub_data)
        if not rows:
            raise
        return rows
