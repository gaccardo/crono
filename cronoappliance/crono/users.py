from django.shortcuts import render
from django.template import RequestContext, loader
from django.db.models import Count, Sum
from django.db.models.query import QuerySet
from django.http import Http404, HttpResponse
from django.utils import simplejson

from crono.models import Access
from squid import squid_helper

sq_helper = squid_helper.SquidHelper()

def all(request):
    return HttpResponse(sq_helper.get_users_as_json())

def update(request):
    return HttpResponse('update')

def add(request):
    return HttpResponse('add')

def delete(request):
    return HttpResponse('delete')
