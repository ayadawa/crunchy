from django.conf.urls import url
from . import views

app_name = 'bookings'
urlpatterns = [
    # ex. bookings/500
    url(r'^(?P<user_id>[0-9]+)/$', views.detail, name='detail'),
]
