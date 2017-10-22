from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import Booking
from hotels.models import Hotel
from .forms import CreateBookingForm


def detail(request, booking_id):
    if request.user.is_authenticated:
        user = request.user
        # hotel = Hotel.objects.get(pk=hotel_id)
        booking = Booking.objects.get(pk=booking_id)
        # only allow access if the booking belongs to the user, maybe instead of 404 we can throw error msg
        # booking = get_object_or_404(Booking, user=user, hotel=hotel)
        context = {
            'user': user,
            'hotel': booking.hotel,
            'booking': booking,
        }
        return render(request, 'bookings/detail.html', context)
    else:
        return redirect('/accounts/login')


def create(request, hotel_id):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = CreateBookingForm(request.POST)

            print(form.errors)

            if form.is_valid():
                hotel = Hotel.objects.get(pk=hotel_id)
                booking = form.save(commit=False)
                booking.hotel = hotel
                booking.user = request.user
                booking.start_date = form.cleaned_data['start_date']
                booking.end_date = form.cleaned_data['end_date']
                booking.start_time = form.cleaned_data['start_time']
                booking.end_time = form.cleaned_data['end_time']
                booking.save()
                url_path = '/bookings/%s' % booking.id
                return redirect(url_path)
            else:
                return redirect('/hotels/' + hotel_id)
        else:
            return Http404()
    else:
        return redirect('/accounts/login')

