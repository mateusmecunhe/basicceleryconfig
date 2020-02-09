from celery import Celery
import time

app = Celery('tasks', broker='amqp://localhost//')

@app.task
def reverse(string, seconds):
    time.sleep(seconds)
    return string[::-1]


# to initialize celery:
# start rabbit in a terminal:
# sudo service rabbitmq-server start
# then initialize celery:
# celery -A tasks worker --loglevel=info
# call function with function.delay()

# when instantiating the Celery instance, you can pass in the backend argument with the url to the DB