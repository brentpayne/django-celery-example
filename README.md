django-celery-example
=====================

This code is a simple running example of using basic celery techniques in django. 

Requirements
============
RabbitMQ
http://www.rabbitmq.com/download.html

Redis
http://redis.io/topics/quickstart

The python packages in _requirements.txt_
  pip install django celery django-celery

Queue tasks
===========

You can use any of the provided django commands to queue tasks. The djano commands are all defined in the polls app under management/commands. Below we use __run\_one\_add__.

  python manage.py run\_one\_add


   
Start a worker
==============

   python manage.py celery worker -c 1
   
Note: the __-c 1__ option limits the worker pool size to one


Further Reading
===============

Celery Docs
http://www.celeryproject.org/tutorials/

Flower: a celery monitor
https://github.com/mher/flower
