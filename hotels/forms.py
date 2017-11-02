from django.forms import ModelForm
from .models import Hotel


class SearchHotelForm(ModelForm):

    class Meta:
        model = Hotel
        fields = ['rating']
