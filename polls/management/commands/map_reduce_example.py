"""
.. container:: creation-info

    Created on 7/30/13

    @author: brentpayne

This is an example of doing a map reduce operation using the
Celery ::map and ::chord functions.
"""


from celery import chord

from django.core.management import BaseCommand
from polls.tasks import square, sum_task
class Command(BaseCommand):

    def handle(self, *args, **options):
        #chord( task_list )( callback )
        task = chord( square.map([1,2,3,4,5]) , sum_task.s())
        status = task.delay()
        rv = status.get()

        print rv
