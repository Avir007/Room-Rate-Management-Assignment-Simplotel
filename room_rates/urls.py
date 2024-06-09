from django.urls import path
from . import views

urlpatterns = [
    path('room_rates/', views.RoomRateListCreateView, name='room_rate_list_create'),
    path('update_room_rates/<int:pk>/', views.RoomRateUpdateView, name='update_room_rate_detail'),
    path('delete_room_rates/<int:pk>/', views.RoomRateDeleteView, name='delete_room_rate_detail'),
    path('overridden_room_rates/', views.OverriddenRoomRateListCreateView, name='overridden_room_rate_detail'),
    path('update_overridden_room_rates/<int:pk>/', views.OverriddenRoomRateUpdateView, name='update_overridden_room_rate_detail'),
    path('delete_overridden_room_rates/<int:pk>/', views.OverriddenRoomRateDeleteView, name='delete_overridden_room_rate_detail'),
    path('discount/', views.DiscountListCreateView, name='discount_detail'),
    path('update_discount/<int:pk>/', views.DiscountUpdateView, name='update_discount_detail'),
    path('delete_discount/<int:pk>/', views.DiscountDeleteView, name='delete_discount_detail'),
    path('discount_room_rates_mapping/', views.DiscountRoomRateMappingView, name='discount_room_rate_mapping_detail'),
    path('update_discount_room_rates_mapping/<int:pk>/', views.DiscountRoomRateMappingUpdateView, name='discount_room_rate_mapping_update_detail'),
    path('update_discount_room_rates_mapping/<int:pk>/', views.DiscountRoomRateMappingUpdateView, name='discount_room_rate_mapping_update_detail'),
    path('room_rate_calculator/<int:room_id>/<str:start_date>/<str:end_date>/', views.CalculatorRatesView, name='calculator-rates'),
    # path('delete_overridden_room_rates/', views.OverriddenRoomRateDeleteView.as_view(), name='delete_overridden_room_rate_detail'),
]