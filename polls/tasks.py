from random import randint
from time import sleep

__author__ = 'brentpayne'

from celery import task

@task()
def add(x, y):
    print add.name, "Add task received", x, y
    return x + y

@task()
def multi(x, y):
    print multi.name, "Multiple task received", x, y
    return x * y

@task
def square(x):
    sleep_time = randint(10, 30)
    sleep(sleep_time)
    return x**2

@task
def sum_task(values):
    return sum(*values)

@task
def first(value):
    print "First task given value:", value
    second.delay(value+1)

@task
def second(value):
    print "Second task given value:", value
