import atexit

from apscheduler.scheduler import Scheduler
from flask import Flask

app = Flask(__name__)

cron = Scheduler(daemon=True)
# Explicitly kick off the background thread
cron.start()

@cron.interval_schedule(hours=1)
def job_function():
    # Do your work here
    print('Hello')


# Shutdown your cron thread if the web process is stopped
atexit.register(lambda: cron.shutdown(wait=False))

if __name__ == '__main__':
    app.run()