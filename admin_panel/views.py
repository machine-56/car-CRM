from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Car
# Create your views here.

def adindex(request):
    return render(request, 'admin_panel/ad_home.html')

def view_all_cars(request):
    cars = Car.objects.all().order_by('-created_at')
    return render(request, 'admin_panel/car_list.html', {'cars': cars})


def edit_car(request, id):
    car = Car.objects.get(id=id)

    if request.method == 'POST':
        # car.name = request.POST.get('name')
        # car.brand = request.POST.get('brand')
        # car.category = request.POST.get('category')
        car.price = request.POST.get('price')
        # car.year_of_manufacture = request.POST.get('year_of_manufacture')
        # car.mileage = request.POST.get('mileage')
        # car.gearbox = request.POST.get('gearbox')
        # car.speed = request.POST.get('speed')
        # car.description = request.POST.get('description')
        # car.available = True if request.POST.get('available') == 'True' else False

        if 'image' in request.FILES:
            car.image = request.FILES['image']

        car.save()
        messages.success(request, 'Car details updated successfully.')
        return redirect('view_all_cars')

    return render(request, 'admin_panel/edit_car.html', {'car': car})
