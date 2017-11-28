from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from bookings.models import Booking

# from ..bookings.models import Booking
# Create your views here.
def reservations(request):
    return render(request, 'viewer/reservations.html')

def previous(request):
    return render(request, 'viewer/previous.html')


def upcoming(request):
    user = request.user
    bookings = Booking.objects.filter(user_id=user.id)
    context = {
        'user': user,
        'bookings': bookings,
    }
    return render(request, 'viewer/upcoming.html', context)

def delete(request, booking_id):
    print('booking id: ' + booking_id)
    # if request.method == "POST":
    Booking.objects.get(id=booking_id).delete()
    return redirect('/viewer/upcoming')
