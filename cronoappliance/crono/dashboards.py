from django.shortcuts import render
from django.template import RequestContext, loader
from django.db.models import Count, Sum
from django.db.models.query import QuerySet
from django.http import Http404, HttpResponse
from django.utils import simplejson

from crono.models import Access

import time

##############
# URL: top10 #
##############
def get_top_ten(request):
	context = RequestContext(request, {})
	return render(request, 'crono/dashboards/sites_info.html', context)

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

def get_sites_range(request, date_from, date_to, page):
	urlXpage = 10
	page = int(page)
	timestamp_from = time.mktime( time.strptime(date_from, '%m_%d_%Y') )
	timestamp_to = time.mktime( time.strptime(date_to, '%m_%d_%Y') )
	accesses = Access.objects.filter(time__gte=timestamp_from,
		                               time__lt=timestamp_to).values('url').annotate(count=Count('url')).order_by('-count')[page*urlXpage:page*urlXpage+urlXpage]
	result_accesses = list()

	for acc in accesses:
		result_accesses.append({'url': acc['url'], 'count': acc['count']})

	return HttpResponse(simplejson.dumps({'urls': result_accesses}))

def get_traffic_range(request, date_from, date_to):
	timestamp_from = time.mktime( time.strptime(date_from, '%m_%d_%Y') )
	timestamp_to = time.mktime( time.strptime(date_to, '%m_%d_%Y') )

	accesses = Access.objects.filter(time__gte=timestamp_from,
		                               time__lt=timestamp_to).annotate(Sum('data'))

	result = 0

	for access in accesses:
		result += access.data

	return HttpResponse(simplejson.dumps({'traffic': result}))
##################
# / URL: top10 / #
##################

###############
# URL: sites  #
###############
def site(request, site):
	date_from = request.GET.get('from', '')
	date_to = request.GET.get('to', '')
	site_orig = site
	site = site.upper()
	site = site.replace('_','.')
	context = RequestContext(request, {'sitename': site,
	                                   'originalsitename': site_orig,
	                                   'date_from': date_from,
	                                   'date_to': date_to})
	return render(request, 'crono/dashboards/site.html', context)

def sitebackend(request, site, date_from, date_to):
	timestamp_from = time.mktime( time.strptime(date_from, '%m_%d_%Y') )
	timestamp_to = time.mktime( time.strptime(date_to, '%m_%d_%Y') )
	accesses = Access.objects.filter(time__gte=timestamp_from,
		                               time__lt=timestamp_to,
		                               url=site.replace('_','.')).values('ip').annotate(count=Count('ip'))
	result_accesses = list()

	for acc in accesses:
		result_accesses.append({'ip': acc['ip'], 'count': acc['count']})

	return HttpResponse(simplejson.dumps({'ips': result_accesses}))
##################
# / URL: sites / #
##################
