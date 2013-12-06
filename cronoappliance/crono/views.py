from django.shortcuts import render, render_to_response, redirect
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.context_processors import csrf

# Create your views here.

#@login_required
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

def firewall(request):
	context = RequestContext(request, {
		'hola': 'hola'
	})
	return render(request, 'crono/proxy.html', context)

def configuration(request):
	context = RequestContext(request, {
		'hola': 'hola'
	})
	return render(request, 'crono/proxy.html', context)

def login_user(request):
    state = "Please log in below..."
    username = password = ''
    c = {}
    c.update(csrf(request))
    state_code = 0
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                state = "You're successfully logged in!"
                state_code = 0
            else:
                state = "Your account is not active, please contact the site admin."
               	state_code = 1
        else:
            state = "Your username and/or password were incorrect."
            state_code = 1

    return render_to_response('crono/auth.html', RequestContext(request, {'state':state, 'username': username,
    	                                                                    'state_code': state_code}))

def logout_user(request):
	logout(request)
	return redirect('/accounts/login/?next=%s' % request.path)