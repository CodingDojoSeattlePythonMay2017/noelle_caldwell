from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^processmoney$', views.process, name='process'),
    url(r'^reset$', views.reset, name='reset')
]
