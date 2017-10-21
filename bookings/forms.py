from django import forms
from django.forms import ModelForm
from .models import Booking


class DateInput(forms.DateInput):
    input_type = 'date'


class CreateBookingForm(ModelForm):

    class Meta:
        model = Booking
        fields = ['start_date', 'end_date', 'start_time', 'end_time']
        widgets = {
            'start_date': DateInput(),
            'end_date': DateInput(),
        }



