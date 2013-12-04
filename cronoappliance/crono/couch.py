from couchbase import Couchbase
from couchbase.views.iterator import View, Query

from django.http import Http404, HttpResponse
from django.utils import simplejson

def last_key(request):

	cb = Couchbase.connect(bucket='default')
	value = cb.get('last_key').value

	return HttpResponse(simplejson.dumps({'last_key': value}))

# By Code
def denied_requests(request):
	cb = Couchbase.connect(bucket='default')
	q = Query()
	q.limit = 100

	denied_requests = list()

	for result in View(cb, "by_code", "denies", query=q):
		denied_requests.append(result.value)

	return HttpResponse(simplejson.dumps({'denied_sites': denied_requests}))

def misses_requests(request):
	cb = Couchbase.connect(bucket='default')
	q = Query()
	q.limit = 100

	misses_requests = list()

	for result in View(cb, "by_code", "misses", query=q):
		misses_requests.append(result.value)

	return HttpResponse(simplejson.dumps({'misses_sites': misses_requests}))

def misses_requests_by_time_range(request, init_time=None, finish_time=None):
	cb = Couchbase.connect(bucket='default')
	q = Query()
	if init_time is not None and finish_time is not None:
		q.mapkey_range = [init_time.replace('_', '.'), finish_time.replace('_', '.')]

	q.limit = 100

	misses_requests = list()

	for result in View(cb, "by_code", "misses", query=q):
		misses_requests.append(result.value)

	return HttpResponse(simplejson.dumps({'misses_sites': misses_requests,
		                                    'init_time': init_time,
		                                    'finish_time': finish_time}))

# By IP
def denies_by_ip(request):
	cb = Couchbase.connect(bucket='default')
	q = Query()
	q.limit = 100

	denies_requests = list()

	for result in View(cb, "by_ip", "denied", query=q):
		denies_requests.append(result.value)

	return simplejson.dumps({'denies_by_ip': denies_requests})