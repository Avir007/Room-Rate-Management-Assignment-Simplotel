from django.contrib import admin
from .models import *

admin.site.register(RoomRate)
admin.site.register(OverriddenRoomRate)
admin.site.register(Discount)
admin.site.register(DiscountRoomRate)

# Register your models here.
