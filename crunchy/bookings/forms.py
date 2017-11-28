from django import forms
from django.forms import ModelForm
from .models import Booking
from bookings.models import Booking
from hotels.models import Hotel


class DateInput(forms.DateInput):
    input_type = 'date'


# class CreateBookingForm(ModelForm):
#
#     class Meta:
#         model = Booking
#
#         fields = ['check_in_date', 'check_out_date']
#         labels = {
#             'check_in_date': "Check in",
#             'check_out_date': "Check out",
#         }
#         widgets = {
#             'check_in_date': DateInput(),
#             'check_out_date': DateInput(),
#
#         }

class CreateBookingForm(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        self.id = kwargs.pop('id', None)
        super(CreateBookingForm, self).__init__(*args, **kwargs)

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


    def clean(self):
            hotel = Hotel.objects.get(pk=self.id)
            if Booking.objects.filter(hotel=hotel).exists():
                ck_in = self.cleaned_data['check_in_date']
                ck_out = self.cleaned_data['check_out_date']

                if ck_in <= ck_out:
                    print("check in smaller than check out")

                for bk_object in Booking.objects.filter(hotel = hotel):
                    bkc_in = bk_object.check_in_date
                    bkc_out = bk_object.check_out_date

                    print("----")

                    print(bkc_in)
                    print(bkc_out)

                    #if bkc_in <= ck_in <= bkc_out or bkc_in <= ck_out <= bkc_out: #trying to book when its booked already
                        #print("ERRORORORORORROROROROR")
                        #raise forms.ValidationError("Sorry this hotel is booked during this time period, please pick another")



                    if ck_in <= bkc_out and  ck_out >= bkc_in:
                        raise forms.ValidationError("This hotel is booked during this time period, please pick another")

                    #StartA <= EndB) and (EndA >= StartB)






