from django.shortcuts import render, get_object_or_404, redirect
from .models import Hotel
from bookings.forms import CreateBookingForm
from .forms import SearchHotelForm
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    hotels_list = Hotel.objects.all()
    form = SearchHotelForm()
    paginator = Paginator(hotels_list, 15) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        hotels = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        hotels = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        hotels = paginator.page(paginator.num_pages)

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

