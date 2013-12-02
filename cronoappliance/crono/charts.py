import random

from django.shortcuts import render
#from crono.models import Dashboard, Graph
from django.template import RequestContext, loader
from django.http import Http404, HttpResponse
from django.utils import simplejson

# Json for charts
def gauge(request, graph_id):
	try:
		graph = Graph.objects.filter(pk=graph_id)

		angularjson = dict()
		angularjson["scale"] = dict()
		angularjson["scale"]["startValue"] = graph[0].startvalue
		angularjson["scale"]["endValue"] = graph[0].stopvalue
		angularjson["scale"]["majorTick"] = dict()
		angularjson["scale"]["majorTick"]["color"] = "black"
		angularjson["scale"]["majorTick"]["tickInterval"] = graph[0].majortick
		angularjson["scale"]["minorTick"] = dict()
		angularjson["scale"]["minorTick"]["color"] = "black"
		angularjson["scale"]["minorTick"]["tickInterval"] = graph[0].minortick
		angularjson["rangeContainer"] = dict()
		angularjson["rangeContainer"]["backgroundColor"] = "none"
		angularjson["rangeContainer"]["ranges"] = list()
		angularjson["rangeContainer"]["ranges"].append({'startValue': graph[0].greefrom,
			                                              'endValue': graph[0].greeto,
			                                              'color': "#A6C567"})
		angularjson["rangeContainer"]["ranges"].append({'startValue': graph[0].yellowfrom,
			                                              'endValue': graph[0].yellowto,
			                                              'color': "#FCBB69"})
		angularjson["rangeContainer"]["ranges"].append({'startValue': graph[0].redfrom,
			                                              'endValue': graph[0].redto,
			                                              'color': "#E19094"})

		value = random.uniform(0,2000)
		angularjson["needles"] = [{'value': value, 'width': 4}]
		angularjson["markers"] = [{'value': value}]

	except Graph.DoesNotExist:
		raise Http404

	return HttpResponse(simplejson.dumps(angularjson))