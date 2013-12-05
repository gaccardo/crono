from django.http import Http404, HttpResponse
from django.utils import simplejson
from django.core.urlresolvers import reverse

def represent(request):
	menu = list()

	menu.append( ('Dashboards', 'dashboard', 'dashboard', reverse('dashboard', args=[])) )
	#menu.append( ('Reports', '', 'bar-chart-o') )
	menu.append( ('Firewall', 'firewall', 'wrench', reverse('firewall', args=[])) )
	menu.append( ('Proxy', 'proxy', 'edit', reverse('proxy', args=[])) )
	menu.append( ('Configuration', 'conf', 'wrench', reverse('configuration', args=[])) )

	return HttpResponse(simplejson.dumps(menu))