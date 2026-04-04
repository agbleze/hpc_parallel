from celery import Celery

app = Celery("tasks", broker="pyamqp://guest@localhost//",
             backend="rpc://"
             )


@app.task
def my_task():
    return "This is a task"

@app.task
def add(x, y):
    return x + y

@app.task
def mul(x, y):
    return x * y

@app.task
def xsum(numbers):
    return sum(numbers)