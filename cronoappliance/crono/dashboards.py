from django.shortcuts import render
from django.template import RequestContext, loader
from django.db.models import Count
from django.db.models.query import QuerySet
from django.http import Http404, HttpResponse
from django.utils import simplejson

from crono.models import Access

import time

#######################
# URL: top10 frontend #
#######################
def get_top_ten(request):
	context = RequestContext(request, {})
	return render(request, 'crono/dashboards/top_ten.html', context)

def get_top_ten_range(request, date_from, date_to):
	timestamp_from = time.mktime( time.strptime(date_from, '%m_%d_%Y') )
	timestamp_to = time.mktime( time.strptime(date_to, '%m_%d_%Y') )
	accesses = Access.objects.filter(time__gte=timestamp_from,
		                               time__lt=timestamp_to).values('url').annotate(count=Count('url')).order_by('-count')[0:10]
	result_accesses = list()

	for acc in accesses:
		result_accesses.append({'url': acc['url'], 'count': acc['count']})

	return HttpResponse(simplejson.dumps({'urls': result_accesses}))

def get_top_ten_denied_range(request, date_from, date_to):
	timestamp_from = time.mktime( time.strptime(date_from, '%m_%d_%Y') )
	timestamp_to = time.mktime( time.strptime(date_to, '%m_%d_%Y') )
	accesses = Access.objects.filter(time__gte=timestamp_from,
		                               time__lt=timestamp_to,
		                               code__startswith='TCP_DENIED').values('url').annotate(count=Count('url')).order_by('-count')[0:10]
	result_accesses = list()

	for acc in accesses:
		result_accesses.append({'url': acc['url'], 'count': acc['count']})

	return HttpResponse(simplejson.dumps({'urls': result_accesses}))
###########################
# / URL: top10 frontend / #
###########################