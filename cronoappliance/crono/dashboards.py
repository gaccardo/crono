from django.shortcuts import render
from django.template import RequestContext, loader
from django.db.models import Count
from django.db.models.query import QuerySet
from django.http import Http404, HttpResponse
from django.utils import simplejson

from crono.models import Access

import time

def get_ips_info(request):
	"""
	cb = Couchbase.connect(bucket='default')
	all_requests = list()
	denies_requests = list()
	hits_requests = list()
	misses_requests = list()
	final_requests = list()

	# all
	q = Query()
	q.group = True
	q.group_level = 1
	for result in View(cb, "by_ip", "all", query=q):
		all_requests.append( {'ip': result.key} )

	# denies
	q = Query()
	q.group = True
	q.group_level = 1
	for result in View(cb, "by_ip", "denied", query=q):
		denies_requests.append( {'ip': result.key, 'denies': result.value} )

	# hists
	q = Query()
	q.group = True
	q.group_level = 1
	for result in View(cb, "by_ip", "hits", query=q):
		hits_requests.append( {'ip': result.key, 'hits': result.value} )	

	# misses
	q = Query()
	q.group = True
	q.group_level = 1
	for result in View(cb, "by_ip", "misses", query=q):
		misses_requests.append( {'ip': result.key, 'misses': result.value} )

	
	for ip in all_requests:
		tmp = {'ip': ip['ip']}

		for iip in denies_requests:
			if iip['ip'] == ip['ip']:
				tmp['denies'] = iip['denies']			

		for iip in misses_requests:
			if iip['ip'] == ip['ip']:
				tmp['misses'] = iip['misses']

		for iip in hits_requests:
			if iip['ip'] == ip['ip']:
				tmp['hits'] = iip['hits']

		final_requests.append(tmp)
	
	print final_requests
	context = RequestContext(request, {
		'ip_stats': final_requests
	})
	return render(request, 'crono/dashboards/deniesbyip.html', context)
	"""
	pass

def get_top_ten(request):
	context = RequestContext(request, {})
	return render(request, 'crono/dashboards/top_ten.html', context)

	#timestamp = time.mktime( time.strptime(datestring, '%d/%m/%Y') )

def get_top_ten_range(request, date_from, date_to):
	timestamp_from = time.mktime( time.strptime(date_from, '%m_%d_%Y') )
	timestamp_to = time.mktime( time.strptime(date_to, '%m_%d_%Y') )
	
	accesses = Access.objects.filter(time__gte=timestamp_from,
		                               time__lt=timestamp_to).values('url').annotate(count=Count('url')).order_by('-count')[0:10]
	result_accesses = list()

	for acc in accesses:
		result_accesses.append({'url': acc['url'], 'count': acc['count']})

	return HttpResponse(simplejson.dumps({'urls': result_accesses}))