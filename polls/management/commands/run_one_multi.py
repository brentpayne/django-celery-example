'''
.. container:: creation-info

    Created on 7/30/13

    @author: brentpayne

TODO: document frame's intent. The framer is brentpayne
'''

from django.core.management import BaseCommand
from polls.tasks import add, multi
class Command(BaseCommand):

    def handle(self, *args, **options):
        status = multi.delay(4, 6)
        rv = status.get()
        print rv