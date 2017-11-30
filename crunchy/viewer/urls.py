from django.conf.urls import url
from . import views

app_name = 'viewer'
urlpatterns = [
    url(r'^$', views.reservations, name='reservations'),
    url(r'^previous/$', views.previous, name='previous'),
    url(r'^upcoming/$', views.upcoming, name='upcoming'),

    # ex. bookings/500/delete
    # url(r'^(?P<booking_id>[0-9]+)/delete/$', views.delete, name='delete'),
    url(r'^upcoming/delete/(?P<booking_id>[0-9]+)$', views.delete, name='delete'),

    # url(r'^upcoming/delete/$', views.delete, name='delete')

]

