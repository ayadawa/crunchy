from django.conf.urls import url
from . import views

app_name = 'accounts'
urlpatterns = [
    # ex. accounts/register
    url(r'^register/$', views.register_user, name='register'),
    # ex. accounts/login
    url(r'^login/$', views.login_user, name='login'),
    # ex. accounts/logout
    url(r'^logout/$', views.logout_user, name='logout'),
    # ex. accounts/500
    url(r'^(?P<user_id>[0-9]+)/$', views.profile_user, name='profile'),

    url(r'^rewards/$', views.rpoints, name='rewards'),
]