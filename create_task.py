from app import db, TaskList

"""
first_task = TaskList(text="Have Lunch")
db.session.add(first_task)
db.session.commit()

second_task = TaskList(text="Write Code")
db.session.add(second_task)
db.session.commit()

third_task = TaskList(text="Date Night")
db.session.add(third_task)
db.session.commit()
"""

# grabbing all tasks
all_tasks = TaskList.query.all()
for task in all_tasks:
    print(task)
