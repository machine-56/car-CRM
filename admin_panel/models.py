from django.db import models

# Create your models here.
class Car(models.Model):
    CATEGORY_CHOICES = [
        ('sedan', 'Sedan'),
        ('suv', 'SUV'),
        ('sports', 'Sports Car'),
        ('electric', 'Electric'),
        ('luxury', 'Luxury'),
    ]

    GEARBOX_CHOICES = [
        ('manual', 'Manual'),
        ('automatic', 'Automatic'),
        ('hybrid', 'Hybrid'),
    ]

    SPEED_CHOICES = [
        ('4-speed', '4-Speed'),
        ('5-speed', '5-Speed'),
        ('6-speed', '6-Speed'),
        ('7-speed', '7-Speed'),
        ('8-speed', '8-Speed'),
    ]

    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='car_images/')
    price = models.DecimalField(max_digits=12, decimal_places=2)
    available = models.BooleanField(default=True)

    # Detailed specs
    year_of_manufacture = models.PositiveIntegerField()
    mileage = models.CharField(max_length=50)  # e.g., "15 km/l" or "350 km/charge"
    gearbox = models.CharField(max_length=20, choices=GEARBOX_CHOICES)
    speed = models.CharField(max_length=10, choices=SPEED_CHOICES)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)