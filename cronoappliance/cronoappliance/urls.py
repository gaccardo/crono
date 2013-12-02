from django.conf.urls import patterns, include, url

from crono import views, menu

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cronoappliance.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^crono/dashboard', 'crono.views.dashboard', name='dashboard'),
    url(r'^crono/proxy', 'crono.views.proxy', name='proxy'),
    url(r'^backend/menu/', menu.represent, name='menu'),
    url(r'^backend/layout', 'crono.views.layout', name='layout'),
)
