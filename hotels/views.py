from django.shortcuts import render, get_object_or_404, redirect
from .models import Hotel
from bookings.forms import CreateBookingForm
from .forms import SearchHotelForm
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from . import placeid


def index(request):
    hotels_list = Hotel.objects.all()
    form = SearchHotelForm()
    paginator = Paginator(hotels_list, 52)  # Show 52 hotels per page

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
    form = CreateBookingForm(None)
    hotel = get_object_or_404(Hotel, pk=hotel_id)
    place_id = placeid.get_hotel_id(hotel_id)
    context = {
        'hotel': hotel,
        'form': form,
        'range': range(1, 6),
        'hotel_rating': round(hotel.rating, 0),
    }

    context['p_id'] = place_id


    print(place_id)
    return render(request, 'hotels/detail.html', context)


def search(request):
    if request.method == "GET":
        form = SearchHotelForm(request.GET)
        if form.is_valid():
            price_bound = {
                # arbitrary large number
                0.0: [0, 999999],
                0: [0, 999999],
                1: [0, 50],
                2: [50, 100],
                3: [100, 150],
                4: [150, 200],
                5: [200, 999999]
            }

            rating = form.cleaned_data['rating']
            price_range = price_bound[form.cleaned_data['price']]
            city_name = form.cleaned_data['city'].strip()
            if city_name == "":
                print('price range city name null: %s %s' % (price_range[0], price_range[1]))
                hotels = Hotel.objects.filter(rating__lte=rating, price__gt=price_range[0],
                                              price__lte=price_range[1]).order_by('-rating')
            else:
                print('price range city name valid: %s %s %s' % (city_name, price_range[0], price_range[1]))
                hotels = Hotel.objects.filter(rating__lte=rating, price__gt=price_range[0],
                                              price__lte=price_range[1], city=city_name).order_by('-rating')
            context = {
                'hotels': hotels,
                'form': form,
            }
            return render(request, 'hotels/index.html', context)
        else:
            return redirect('/hotels/hotels/')
    else:
        return Http404()

# Easy to use API call to fetch a list of hotels, AKA Search functionality
# ex. hotels/search/location/<city_name>/price/<tag>/rating/<rating>
# def search(request, city_name, price, rating):
#     if request.method == "GET":
#         price_bound = {
#             # arbitrary large number
#             '0': [0, 999999],
#             1: [0, 50],
#             2: [50, 100],
#             3: [100, 150],
#             4: [150, 200],
#             5: [200, 999999]
#         }
#         # not handling any edges cases AT ALL!
#         city_name = city_name.strip
#         price_range = price_bound[price]
#         if rating == 0:
#             rating = 5
#
#         if city_name == "":
#             hotels = Hotel.objects.filter(rating__lte=rating, price__gt=price_range[0],
#                                           price__lte=price_range[1]).order_by('-rating')
#         else:
#             hotels = Hotel.objects.filter(rating__lte=rating, price__gt=price_range[0],
#                                           price__lte=price_range[1], city=city_name).order_by('-rating')
#         context = {
#             'hotels': hotels,
#         }
#         return render(request, 'hotels/index.html', context)
#     else:
#         return Http404()

