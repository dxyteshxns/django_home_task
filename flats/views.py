from django.shortcuts import render
from flats.models import Flat


def flats_list(request):
    all_flats = Flat.objects.filter(available=True)
    return render(request, 'flats_list.html', context={
        'all_flats': all_flats
    })
