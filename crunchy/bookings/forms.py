from django import forms
from django.forms import ModelForm
from .models import Booking


class DateInput(forms.DateInput):
    input_type = 'date'


class CreateBookingForm(ModelForm):

    class Meta:
        model = Booking

        fields = ['check_in_date', 'check_out_date']
        labels = {
            'check_in_date': "Check in",
            'check_out_date': "Check out",
        }
        widgets = {
            'check_in_date': DateInput(),
            'check_out_date': DateInput(),

        }



