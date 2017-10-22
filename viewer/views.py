from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.
def reservations(request):

    return render(request, 'viewer/reservations.html')

