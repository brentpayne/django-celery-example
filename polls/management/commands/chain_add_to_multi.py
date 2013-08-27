'''
.. container:: creation-info

    Created on 7/30/13

    @author: brentpayne

TODO: document frame's intent. The framer is brentpayne
'''
from celery import chain

from django.core.management import BaseCommand
from polls.tasks import add, multi
class Command(BaseCommand):

    def handle(self, *args, **options):
        addsub = add.s(4)
        status = chain( add.s(2,2)| addsub | multi.s(2))()
        rv = status.get()
        print rv
