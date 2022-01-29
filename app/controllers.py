from .app import app, db
from .models import Todo

from flask import request, url_for, redirect, jsonify

#controlador para adicionar uma nova tarefa
@app.route('/add', methods=['POST'])
def add_todo():
    name = request.form.get('todo_name')
    desc = request.form.get('todo_desc')
    new_todo = Todo(name, desc)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for('home'))

#controlador para atualizar o estado da tarefa
@app.route('/update/<int:todo_id>', methods=['GET'])
def update_todo(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    if todo:
        if todo.state == False:
            todo.state = True
            db.session.commit()
            return redirect(url_for('home'))
        else:
            todo.state = False
            db.session.commit()
            return redirect(url_for('home'))
    else:
        return jsonify({
            'error': True,
            'message': f'todo {todo_id} not found'
        })


#controlador para remover uma tarefa
@app.route('/delete/<int:todo_id>', methods=['GET'])
def remove_todo(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    if todo:
        db.session.delete(todo)
        db.session.commit()
        return redirect(url_for('home')) 
    else:
        return jsonify({
            'error': True,
            'message': f'todo {todo_id} not found'
        })