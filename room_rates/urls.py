from django.urls import path
from . import views

urlpatterns = [
    path('room_rates/', views.RoomRateListCreateView, name='room_rate_list_create'),  #API Endpoint for RoomRate listing and creating new Room Rate
    path('update_room_rates/<int:pk>/', views.RoomRateUpdateView, name='update_room_rate_detail'),  #API Endpoint for RoomRate Updating Existing Room Rate based on pk
    path('delete_room_rates/<int:pk>/', views.RoomRateDeleteView, name='delete_room_rate_detail'),  #API Endpoint for RoomRate deleting existing Room Rate details
    path('overridden_room_rates/', views.OverriddenRoomRateListCreateView, name='overridden_room_rate_detail'),  #API Endpoint for creating and listing Overridden room rate
    path('update_overridden_room_rates/<int:pk>/', views.OverriddenRoomRateUpdateView, name='update_overridden_room_rate_detail'),  # API Endpoint for updating overridden roo rate price  based on pk
    path('delete_overridden_room_rates/<int:pk>/', views.OverriddenRoomRateDeleteView, name='delete_overridden_room_rate_detail'),  #API Endpoint for deletiing overridden raoom rate price
    path('discount/', views.DiscountListCreateView, name='discount_detail'),  #API Endpoint for creating and listing Discount coupon
    path('update_discount/<int:pk>/', views.DiscountUpdateView, name='update_discount_detail'),  #API End point for updating discount as per pk
    path('delete_discount/<int:pk>/', views.DiscountDeleteView, name='delete_discount_detail'),  #API End point for deleting discount as per pk
    path('discount_room_rates_mapping/', views.DiscountRoomRateMappingView, name='discount_room_rate_mapping_detail'),  # API Endpoint for room rate to discount mapping
    path('update_discount_room_rates_mapping/<int:pk>/', views.DiscountRoomRateMappingUpdateView, name='discount_room_rate_mapping_update_detail'),  #API Endpoint for deleting and updatig Roomrate to discount mapping as per key
    path('room_rate_calculator/<int:room_id>/<str:start_date>/<str:end_date>/', views.CalculatorRatesView, name='calculator-rates'),  #API End point for Calculating min price for date range for particular room
]