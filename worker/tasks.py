from celery import Celery

app = Celery("tasks", broker="amqp://localhost",    backend="redis://localhost:6379/0"  )


@app.task
def add(x,y):
    return x+y

"""
1. Create tasks here.
2. Push the tasks to mqtt
3. Worker picks up the tasks, and execute it.
"""