from flask import Flask, render_template, request, redirect, url_for
from src.auth.service import TodoService
    

app = Flask(__name__)
todo_service = TodoService()

@app.route('/')
def index():
    """ Display all tasks."""
    data = todo_service.get_all_todo()
    return render_template("index.html",tasks=data)

@app.route('/about', methods=["POST"])
def add_task():
    """ Adds a new task"""
    description = request.from["description"]
    title = request.from["title"]
    
    return ""

if __name__ == '__main__':
    app.run(debug=True)