
from django.conf.urls import patterns

from . import views

urlpatterns = patterns('',
    (r'^$', views.index),
    (r'^list/$', views.template_list),
    (r'^open/$', views.template_detail),
)
