from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker

today = datetime.today()
engine = create_engine('sqlite:///todo.db?check_same_thread=False')
check_same_thread=False
Base = declarative_base()

class Task(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    string_field = Column("task", String, default='default_value')
    date_field = Column("deadline", Date, default=datetime.today())

    def __repr__(self):
        return self.string_field


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def add_task():
    print("Enter task:")
    new_task = input()
    print("Enter deadline YYYY-MM-DD")
    year, month, day = input().split("-")
    task_deadline = datetime(int(year), int(month), int(day))
    new_row = Task(string_field=new_task, date_field=task_deadline.date())
    session.add(new_row)
    session.commit()
    print("The task has been added!")
    print()


def today_tasks():
    rows = session.query(Task).filter(Task.date_field == today.date()).all()
    if rows == []:
        print("Today", today.day, today.strftime("%b"))
        print("Nothing to do!")
    else:
        print("Today", today.day, today.strftime("%b"))
        for first_row in rows:
            print(str(first_row.id) + ". " + first_row.string_field)
    print()


def weeks_task():
    weekday = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    print()
    for days in range(7):
        week_today = today + timedelta(days=days)
        rows = session.query(Task).filter(Task.date_field == week_today.date()).all()
        if rows == []:
            print(weekday[week_today.weekday()], week_today.day, week_today.strftime("%b"))
            print("Nothing to do!")
            print()
        else:
            print(weekday[week_today.weekday()], week_today.day, week_today.strftime("%b"))
            i = 1
            for first_row in rows:
                print(str(1) + ". " + first_row.string_field)
                i += 1
            print()


def all_task():
    rows = session.query(Task).order_by(Task.date_field).all()
    sorted_taskid_by_date = []
    if rows == []:
        print("Nothing to do!")
    else:
        i = 1
        for first_row in rows:
            task_date = first_row.date_field
            print(str(i) + ". " + first_row.string_field +
                  ". " + str(task_date.day) + " " + str(task_date.strftime("%b")))
            sorted_taskid_by_date.append(first_row.id)
            i += 1
    print()
    return sorted_taskid_by_date


def missed_task():
    print()
    print("Missed tasks:")
    rows = session.query(Task).filter(Task.date_field < today.date()).all()
    if rows == []:
        print("Nothing is missed!")
    else:
        i = 1
        for row in rows:
            task_date = row.date_field
            print(str(i) + ". " + row.string_field + " " + str(task_date.day) + " " +
                  str(task_date.strftime("%b")))
            i += 1
    print()


def delete_task():
    print()
    print("Choose the number of the task you want to delete:")
    task_id = list(all_task())
    try:
        task_to_delete = int(input())
        if task_to_delete > 0 and task_to_delete <= len(task_id):
            row_del = session.query(Task).filter(Task.id == task_id[task_to_delete - 1]).all()
            session.delete(row_del[0])
            session.commit()
            print("The task has been deleted!")
        else:
            print("Invalid number!")
    except:
        print()
    print()

while True:
    choice = input("""1) Today's tasks
2) Week's tasks
3) All tasks
4) Missed tasks
5) Add task
6) Delete task
0) Exit\n""")

    if choice == "1":
        today_tasks()
    elif choice == "2":
        weeks_task()
    elif choice == "3":
        print()
        print("All tasks:")
        all_task()
    elif choice == "4":
        missed_task()
    elif choice == "5":
        add_task()
    elif choice == "6":
        delete_task()
    elif choice == "0":
        print("\nBye!")
        break
