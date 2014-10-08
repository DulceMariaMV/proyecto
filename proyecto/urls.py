from django.conf.urls import patterns, include, url
from django.contrib import admin
from proyecto.apps.usuarios.views import *
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'proyecto.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',inicio_view),
    url(r'^perfil/$',perfil),
   
    url(r'^login/$',login_usuario), 
    url(r'^registro/$',registro),
    
)
