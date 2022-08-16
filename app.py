from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

task_list = ["Have lunch", "Write code", "Date night"]

# creating form object
class TaskForm(FlaskForm):
    task = StringField('Task')
    submit = SubmitField('Add Task')


@app.route('/', methods=["GET", "POST"])
def index():
    # accepting new tasks
    # if there is a 'task' attribute in the form
    if 'task' in request.form:
        task_list.append(request.form['task'])

        # template variables will be list with tasks and a new form object
    return render_template('index.html', tasks=task_list, task_form=TaskForm())
