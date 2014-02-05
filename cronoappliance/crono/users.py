from django.shortcuts import render
from django.template import RequestContext, loader
from django.db.models import Count, Sum
from django.db.models.query import QuerySet
from django.http import Http404, HttpResponse
from django.utils import simplejson

from crono.models import Access


def get_users(request):
    users_database_pointer = open('/etc/squid3/passwd', 'r')
    users_database = users_database_pointer.readlines()
    users_database_pointer.close()
    users = list()

    for line in users_database:
        users.append(line.split(':')[0])

    return HttpResponse(simplejson.dumps({'users': users}))
