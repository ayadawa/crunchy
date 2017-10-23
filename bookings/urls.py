from django.conf.urls import url
from . import views

app_name = 'bookings'
urlpatterns = [
    # ex. bookings/500
    url(r'^(?P<booking_id>[0-9]+)/$', views.detail, name='detail'),
    # ex. bookings/create/500
    url(r'^create/(?P<hotel_id>[0-9]+)/$', views.create, name='create'),
    # ex. bookings/500/delete
    url(r'^(?P<booking_id>[0-9]+)/delete/$', views.delete, name='delete'),
    # ex. bookings/view
    url(r'^(?P<booking_id>[0-9]+)/$', views.detail, name='view'),


]
