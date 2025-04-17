from django.shortcuts import render
from admin_panel.models import Car
from collections import OrderedDict


# Create your views here.
def user_home(request):
    categories = ['sedan', 'suv', 'sports', 'electric', 'luxury']
    cars_by_category = OrderedDict()

    for category in categories:
        cars = Car.objects.filter(category=category, available=True).order_by('-created_at')[:4]
        cars_by_category[category] = cars

    return render(request, 'user/user_home.html', {
        'cars_by_category': cars_by_category
    })