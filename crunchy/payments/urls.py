from django.conf.urls import url
from . import views

app_name = 'payments'
urlpatterns = [
    # ex. payments/summary
    url(r'^summary/$', views.summary, name='summary'),
]