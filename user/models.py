from django.db import models
from accounts.models import CustomUser
from admin_panel.models import Car

# Create your models here.
class OrderedCar(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    delivered = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now_add=True)


class TestDrive(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    booked_at = models.DateTimeField(auto_now_add=True)