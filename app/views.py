from .app import app
from .models import Todo

from flask import render_template

#retorna a view do inicio do app
@app.route('/', methods=['GET'])
def home():
    todo_list = Todo.query.all()
    return render_template('todo.html', todo_list=todo_list)

#retorna a view das informações do app
@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')