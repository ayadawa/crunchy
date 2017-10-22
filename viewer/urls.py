from django.conf.urls import url
from . import views

app_name = 'viewer'
urlpatterns = [
    url(r'^$', views.reservations, name='reservations'),
]

