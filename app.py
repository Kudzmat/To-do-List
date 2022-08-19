from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class TaskList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(100), index=True)

    def __repr__(self):
        return f"{self.text}"


#db.create_all()


# creating form object
class TaskForm(FlaskForm):
    task = StringField('Task')
    submit = SubmitField('Add Task')


@app.route('/', methods=["GET", "POST"])
def index():
    # accepting new tasks
    # if there is a 'task' attribute in the form
    if 'task' in request.form:
        db.session.add(TaskList(text=request.form['task']))
        db.session.commit()

        # template variables will be list with tasks and a new form object
    return render_template('index.html', tasks=TaskList.query.all(), task_form=TaskForm())
