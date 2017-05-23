from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ninjas$', views.showAll, name='all'),
    url(r'^ninjas/(?P<color>.+)$', views.showColor, name='color')
]
