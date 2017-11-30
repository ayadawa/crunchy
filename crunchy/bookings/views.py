from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import Booking
from bookings.models import RewardPoint
from hotels.models import Hotel
from .forms import CreateBookingForm
from django.contrib import messages


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
            form = CreateBookingForm(request.POST,id = hotel_id)

            if form.is_valid():
                hotel = Hotel.objects.get(pk=hotel_id)
                booking = form.save(commit=False)
                booking.hotel = hotel
                booking.user = request.user
                booking.start_time = form.cleaned_data['check_in_date']
                booking.end_time = form.cleaned_data['check_out_date']
                booking.save()

                # add reward points based on 10% of price
                new_points = float(hotel.price) * .10
                reward_point = RewardPoint()
                if RewardPoint.objects.filter(user=request.user).exists():
                    rp_object = RewardPoint.objects.get(user=request.user)
                    current_points = rp_object.reward_points
                    total_points = int(current_points + new_points)
                    rp_object.reward_points = total_points
                    rp_object.save()
                else:
                    reward_point.user = request.user
                    reward_point.reward_points = int(new_points)
                    reward_point.save()


                url_path = '/bookings/%s' % booking.id
                messages.info(request, str(int(new_points))+' Reward Points Gained! ')
                return redirect(url_path)
            else:
                messages.info(request,"Could not book, please pick another date to book")
                form = CreateBookingForm()
                return redirect('/hotels/' + hotel_id,form)

        else:
            return Http404()
    else:
        return redirect('/accounts/login')


# delete reservation
def delete(request, booking_id):
    if request.method == "POST":
        booking = Booking.objects.get(pk=booking_id)
        Booking.objects.filter(id=booking_id).delete()
        url_path = '/hotels/%s' % booking.hotel_id
        return redirect(url_path)

