
from django.conf.urls import patterns

from . import views

urlpatterns = patterns('',
    (r'^$', 'django.shortcuts.render', {'template_name': 'grappelli_te/index.html'}),
    (r'^list/$', views.template_list),
    (r'^open/$', views.template_detail),
)
