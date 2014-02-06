from django.conf.urls import patterns, include, url

from crono import views, menu, dashboards, users

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cronoappliance.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^crono/users/update', 'crono.users.update', name='update'),
    url(r'^crono/users/add', 'crono.users.add', name='add'),
    url(r'^crono/users/delete', 'crono.users.delete', name='delete'),
    url(r'^crono/users/', 'crono.users.all', name='all'),

    url(r'^crono/dashboard/top10/', 'crono.dashboards.get_top_ten', name='top10'),
    url(r'^crono/dashboard/site/(?P<site>[-A-Za-z0-9_]+)/', 'crono.dashboards.site', name='site'),
    url(r'^crono/dashboard', 'crono.views.dashboard', name='dashboard'),

    url(r'^crono/proxy', 'crono.views.proxy', name='proxy'),
    url(r'^crono/firewall', 'crono.views.firewall', name='firewall'),
    url(r'^crono/configuration', 'crono.views.configuration', name='configuration'),

    url(r'^accounts/login/$', 'crono.views.login_user', name='login'),
    url(r'^accounts/logout/$', 'crono.views.logout_user', name='logout'),

    url(r'^menu', menu.represent, name='menu'),
    url(r'^backend/layout', 'crono.views.layout'),

    url(r'^backend/top10byrange/(?P<date_from>\w+)/(?P<date_to>\w+)', 'crono.dashboards.get_top_ten_range', name='top10byrange'),
    url(r'^backend/top10deniedbyrange/(?P<date_from>\w+)/(?P<date_to>\w+)', 'crono.dashboards.get_top_ten_denied_range', name='top10deniedbyrange'),
    url(r'^backend/visitedsitesrange/(?P<date_from>\w+)/(?P<date_to>\w+)/(?P<page>\w+)', 'crono.dashboards.get_sites_range', name='visitedsitesrange'),
    url(r'^backend/trafficrange/(?P<date_from>\w+)/(?P<date_to>\w+)', 'crono.dashboards.get_traffic_range', name='trafficrange'),
    url(r'^backend/sitebackend/(?P<site>\w+)/(?P<date_from>\w+)/(?P<date_to>\w+)', 'crono.dashboards.sitebackend', name='sitebackend'),

    #url(r'^couch/last_key', 'crono.couch.last_key', name='last_key'),
	#url(r'^couch/denied_requests', 'crono.couch.denied_requests'),
	#url(r'^couch/misses_requests/$', 'crono.couch.misses_requests'),
)
