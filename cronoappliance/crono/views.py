from django.shortcuts import render
from django.template import RequestContext, loader


# Create your views here.

def layout(request):
	context =	context = RequestContext(request, {})
	return render(request, 'crono/layout.html', context)

def dashboard(request):
	context = RequestContext(request, {
		'hola': 'hola'
	})
	return render(request, 'crono/home.html', context)

def proxy(request):
	context = RequestContext(request, {
		'hola': 'hola'
	})
	return render(request, 'crono/proxy.html', context)