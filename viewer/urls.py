from django.conf.urls import url
from . import views

app_name = 'viewer'
urlpatterns = [
    url(r'^$', views.reservations, name='reservations'),
    url(r'^previous/$', views.previous, name='previous'),
    url(r'^upcoming/$', views.upcoming, name='upcoming')

]

