from django.conf.urls import url
from . import views

app_name = 'hotels'
urlpatterns = [
    # ex. hotels/
    url(r'^$', views.index, name='hotels'),
    # ex. hotels/500
    url(r'^(?P<hotel_id>[0-9]+)/$', views.detail, name='detail'),
    # ex. hotels/search
    url(r'^search/$', views.search, name='search'),
]