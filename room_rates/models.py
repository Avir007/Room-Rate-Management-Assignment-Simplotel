from django.db import models

class RoomRate(models.Model):
    room_id = models.IntegerField()
    room_name = models.CharField(max_length=255)
    default_rate = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.room_name} - {self.default_rate}'

class OverriddenRoomRate(models.Model):
    room_rate = models.ForeignKey(RoomRate, on_delete=models.CASCADE)
    overridden_rate = models.DecimalField(max_digits=10, decimal_places=2)
    stay_date = models.DateField()

    def __str__(self):
        return f'{self.room_rate.room_name} - {self.stay_date} - {self.overridden_rate}'


class Discount(models.Model):
    FIXED = 'fixed'
    PERCENTAGE = 'percentage'
    DISCOUNT_TYPE_CHOICES = [
        (FIXED, 'Fixed'),
        (PERCENTAGE, 'Percentage'),
    ]

    discount_id = models.IntegerField()
    discount_name = models.CharField(max_length=255)
    discount_type = models.CharField(max_length=10, choices=DISCOUNT_TYPE_CHOICES)
    discount_value = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.discount_name} - {self.discount_type} - {self.discount_value}'

class DiscountRoomRate(models.Model):
    room_rate = models.ForeignKey(RoomRate, on_delete=models.CASCADE)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('room_rate','discount')

    def __str__(self):
        return f'{self.room_rate.room_name} - {self.discount.discount_name}'
