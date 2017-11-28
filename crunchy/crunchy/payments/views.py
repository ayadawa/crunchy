from django.shortcuts import render


def summary(request):
	hotel = {
		'name': "hotel1",
		'city': "CA"
	}
	context = {
		'hotel': hotel
	}

	return render(request, 'payments/summary.html', context)

