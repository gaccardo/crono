from django.http import Http404, HttpResponse
from django.utils import simplejson

def represent(request):
	menu = list()

	menu.append( ('Dashboards', '', 'dashboard') )
	menu.append( ('Reports', '', 'bar-chart-o') )
	menu.append( ('Firewall', '', 'wrench') )
	menu.append( ('Proxy', '', 'edit') )
	menu.append( ('Configuration', '', 'wrench') )

	return HttpResponse(simplejson.dumps(menu))