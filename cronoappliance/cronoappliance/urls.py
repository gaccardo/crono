from django.conf.urls import patterns, include, url

from crono import views, menu, couch, dashboards

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cronoappliance.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^crono/dashboard/getIpsInfo', dashboards.get_ips_info, name='getIpsInfo'),
    url(r'^crono/dashboard/$', 'crono.views.dashboard'),

    url(r'^crono/proxy', 'crono.views.proxy'),

    url(r'^menu', menu.represent, name='menu'),
    url(r'^backend/layout', 'crono.views.layout'),

	url(r'^couch/urls_by_ip/(?P<ip>\w+)', couch.urls_by_ip, name='urls_by_ip'),
)
