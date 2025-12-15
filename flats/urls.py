from django.urls import path
from flats.views import flats_list, flat_detail, flat_create


app_name = 'flats'

urlpatterns = [
    path('', flats_list, name='flats_list'),

    path('<int:flat_id>/', flat_detail, name='flat_detail'),

    path('add/', flat_create, name="flat_create")
]