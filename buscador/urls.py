from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #rl(r'^$', 'buscador.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^resultado/', 'app.views.buscar', name='resultado'), 
    url(r'^$', 'app.views.home', name='home'), 
    url(r'^acerca/', 'app.views.acerca', name='acerca'), 
    #url(r'^resultado/', 'app.views.resultado', name='resultado'), 
    url(r'^admin/', include(admin.site.urls)),

)
