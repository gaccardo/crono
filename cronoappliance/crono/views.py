from django.shortcuts import render
from django.template import RequestContext, loader


# Create your views here.

def home(request):
	context = RequestContext(request, {
		'hola': 'hola'
	})
	return render(request, 'crono/home.html', context)