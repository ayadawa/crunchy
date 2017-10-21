from django.shortcuts import render


def detail(request, user_id):
    booking = {
        "user_id": user_id,
        "hotel_id": 1009,
        "start_time": 1234,
        "end_time": 1097,
    }
    user = {
        "user_id": user_id,
        "name": "edward lim",
    }
    context = {
        'booking': booking,
        'user': user,
    }
    return render(request, 'bookings/detail.html', context)

