from django.shortcuts import render, get_object_or_404
from .models import Hotel


def index(request):
    # normally this is how we would fetch data from the database
    hotels = Hotel.objects.all()
    # hotel1 = {
    #     'name': "hotel1",
    #     'img1': 'https://media-cdn.tripadvisor.com/media/photo-s/0d/83/c7/dd/pool.jpg',
    #     'price': "239.00",
    #     'city': "CA",
    # }
    # hotel2 = {
    #     'name': "hotel2",
    #     'img1': 'http://www.cheaprooms.com/images/traveling/hotels/1000000/150000/140600/140596/140596_275_b.jpg',
    #     'price': "559.00",
    #     'city': "LA",
    # }
    # hotels = [hotel1, hotel2]
    context = {
        'hotels': hotels
    }
    return render(request, 'hotels/index.html', context)


def detail(request, hotel_id):
    # normally this is how we would fetch data from the database
    hotel = get_object_or_404(Hotel, pk=hotel_id)
    # hotel = {
    #     'pk': hotel_id,
    #     'name': "hotel2",
    #     'img1': 'http://www.cheaprooms.com/images/traveling/hotels/1000000/150000/140600/140596/140596_275_b.jpg',
    #     'price': "559.00",
    #     'city': "LA",
    # }
    context = {
        'hotel': hotel
    }
    return render(request, 'hotels/detail.html', context)

