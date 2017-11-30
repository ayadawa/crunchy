from django.conf.urls import url
from . import views

app_name = 'hotels'
urlpatterns = [
    # ex. hotels/
    url(r'^hotels/$', views.index, name='hotels'),
    # ex. hotels/500
    url(r'^(?P<hotel_id>[0-9]+)/$', views.detail, name='detail'),
    # ex. hotels/search
    url(r'^search/$', views.search, name='search'),
    # ex. hotels/search/location/<city_name>/price/<tag>/rating/<rating>
    # url(r'^search/location/(?P<city_name>\w+)/price/(?P<price>[0-9]+)/rating/(?P<rating>[0-9]+)/$', views.search, name='search')
]