from django.shortcuts import render, get_object_or_404, redirect
from .models import Hotel
from bookings.forms import CreateBookingForm
from .forms import SearchHotelForm
from django.http import Http404


def index(request):
    hotels = Hotel.objects.all()
    form = SearchHotelForm()
    context = {
        'hotels': hotels,
        'form': form,
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


def search(request):
    if request.method == "GET":
        form = SearchHotelForm(request.GET)
        if form.is_valid():
            rating = form.cleaned_data['rating']
            hotels = Hotel.objects.filter(rating=rating)
            context = {
                'hotels': hotels,
                'form': form,
            }
            return render(request, 'hotels/index.html', context)
        else:
            return redirect('/hotels/')
    else:
        return Http404()

