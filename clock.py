from apscheduler.schedulers.blocking import BlockingScheduler
from main import do_the_job
from datetime import datetime

sched = BlockingScheduler()


@sched.scheduled_job(trigger='cron', hour=9)  # use day_of_week='mon-fri' for workday pass only
def scheduled_job():
    str_today = datetime.today().strftime("%Y-%m-%d")

    print('This job is run every day at 9am.')
    print(str_today)

    do_the_job(str_today)
