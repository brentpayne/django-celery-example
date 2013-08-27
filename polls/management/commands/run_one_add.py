'''
.. container:: creation-info

    Created on 7/30/13

    @author: brentpayne

TODO: document frame's intent. The framer is brentpayne
'''

from django.core.management import BaseCommand
from polls.tasks import add


class Command(BaseCommand):

    def handle(self, *args, **options):
        status = add.delay(4, 6)
        rv = status.get()
        print rv