from django.conf.urls import patterns, include, url

from crono import views, menu, dashboards

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cronoappliance.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    #url(r'^crono/dashboard/getIpsInfo/', dashboards.get_ips_info, name='getIpsInfo'),
    url(r'^crono/dashboard/top10/', 'crono.dashboards.get_top_ten', name='top10'),
    url(r'^crono/dashboard', 'crono.views.dashboard'),

    url(r'^crono/proxy', 'crono.views.proxy'),

    url(r'^menu', menu.represent, name='menu'),
    url(r'^backend/layout', 'crono.views.layout'),

    url(r'^backend/top10byrange/(?P<date_from>\w+)/(?P<date_to>\w+)', 'crono.dashboards.get_top_ten_range', name='top10byrange'),

	#url(r'^couch/last_key', 'crono.couch.last_key', name='last_key'),
	#url(r'^couch/denied_requests', 'crono.couch.denied_requests'),
	#url(r'^couch/misses_requests/$', 'crono.couch.misses_requests'),
)
