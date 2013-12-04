from django.shortcuts import render
from django.template import RequestContext, loader

from couchbase import Couchbase
from couchbase.views.iterator import View, Query


def get_ips_info(request):
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