'''
.. container:: creation-info

    Created on 7/30/13

    @author: brentpayne

TODO: document frame's intent. The framer is brentpayne
'''

import djcelery
from django.core.management import BaseCommand



class Command(BaseCommand):

    def handle(self, *args, **options):
        print djcelery.celery.control.inspect().ping()
        print '-----------------------------------------'
        print djcelery.celery.control.inspect().active_queues()
