import sched
import time 

scheduler = sched.scheduler(time.time, time.sleep)

def soma(n1, n2):
    print(f'A soma is: {n1 + n2} Tempo: {time.ctime()}')
    scheduler.enter(2, 1, soma, (2, 3))

def sub(n1, n2):
    print(f'A sub is: {n1 - n2} Tempo: {time.ctime()}')
    scheduler.enter(2, 1, sub, (2, 3))


def sche():
    scheduler.enter(5, 1, soma, (2, 3))
    scheduler.enter(5, 1, sub, (2, 3))

if __name__=='__main__':
    sche()
    scheduler.run()

