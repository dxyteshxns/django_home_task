from django.urls import path
from flats.views import flats_list, flat_detail, flat_create, flat_edit, flat_delete, send_deal_request, owner_deals_requests_list


app_name = 'flats'

urlpatterns = [
    path('', flats_list, name='flats_list'),

    path('<int:flat_id>/', flat_detail, name='flat_detail'),

    path('add/', flat_create, name="flat_create"),

    path('<int:flat_id>/edit/', flat_edit, name='flat_edit'),

    path('<int:flat_id>/delete/', flat_delete, name='flat_delete'),

    path('<int:flat_id>/deal-request/', send_deal_request, name='send_deal_request'),

    path('my-deal-request/', owner_deals_requests_list, name='owner_deals_requests_list')
]