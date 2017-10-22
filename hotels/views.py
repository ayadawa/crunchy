from django.shortcuts import render, get_object_or_404
from .models import Hotel
from bookings.forms import CreateBookingForm


def index(request):
    hotels = Hotel.objects.all()
    context = {
        'hotels': hotels
    }
    return render(request, 'hotels/index.html', context)


def detail(request, hotel_id):
    form = CreateBookingForm()
    hotel = get_object_or_404(Hotel, pk=hotel_id)
    context = {
        'hotel': hotel,
        'form': form
    }
    return render(request, 'hotels/detail.html', context)

