import sched
import time
from datetime import datetime, timedelta


scheduler = sched.scheduler(time.time, time.sleep)

def soma (n1, n2):
    print(f'Soma: {n1 + n2} tempo: {time.ctime()}')
    scheduler.enterabs((datetime.now() + timedelta(hours=24)).timestamp(), 1, soma, (2, 2))

def sche():
    scheduler.enterabs(datetime(year=2022, month=6, day=3, hour=17, minute=31).timestamp(), 1, soma, (2, 3))

sche()

scheduler.run()

