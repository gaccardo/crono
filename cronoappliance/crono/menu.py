from django.http import Http404, HttpResponse
from django.utils import simplejson

def represent(request):
	menu = list()

	menu.append( ('Dashboards', 'dashboard', 'dashboard') )
	#menu.append( ('Reports', '', 'bar-chart-o') )
	menu.append( ('Firewall', '', 'wrench') )
	menu.append( ('Proxy', 'proxy', 'edit') )
	menu.append( ('Configuration', 'conf', 'wrench') )

	return HttpResponse(simplejson.dumps(menu))