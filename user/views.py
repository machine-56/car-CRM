from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from admin_panel.models import Car
from admin_panel.models import Car
from collections import OrderedDict
from .models import OrderedCar, TestDrive

from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone
from datetime import timedelta

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

@login_required
def car_detail(request, car_id):
    car = Car.objects.get(id=car_id)

    if request.method == "POST":
        existing_order = OrderedCar.objects.filter(user=request.user, delivered=False).first()
        if existing_order:
            messages.error(request, "You already have a car in production or shipping. Please wait until it's delivered.")
        else:
            OrderedCar.objects.create(user=request.user, car=car)
            messages.success(request, "Your order has been placed successfully!")
            return redirect('user_home')

    return render(request, 'user/car_detail.html', {'car': car})

@login_required
def my_orders(request):
    orders = OrderedCar.objects.filter(user=request.user).select_related('car')

    production_times = {
        'sedan': 2,
        'suv': 3,
        'sports': 6,
        'electric': 4,
        'luxury': 12,
    }

    shipping_windows = {
        'sedan': 5,
        'suv': 7,
        'sports': 10,
        'electric': 7,
        'luxury': 14,
    }

    now = timezone.now()

    for order in orders:
        cat = order.car.category
        months = production_times.get(cat, 4)
        shipping_days = shipping_windows.get(cat, 7)

        delivery_date = order.order_date + timedelta(days=30 * months)
        order.estimated_delivery = delivery_date

        if order.delivered:
            order.status = "Delivered"
        elif now >= delivery_date - timedelta(days=shipping_days):
            order.status = "Shipping"
        else:
            order.status = "In Production"

    return render(request, 'user/my_orders.html', {'orders': orders})

@login_required
def book_test_drive(request):
    cars = Car.objects.filter(available=True)

    if request.method == 'POST':
        car_id = request.POST.get('car')
        date = request.POST.get('date')
        time = request.POST.get('time')

        car = Car.objects.get(id=car_id)

        if TestDrive.objects.filter(user=request.user, car=car, date=date, time=time).exists():
            messages.error(request, "You've already booked this test drive slot.")
        else:
            TestDrive.objects.create(user=request.user, car=car, date=date, time=time)
            subject = 'Aurelius Motors – Test Drive Confirmed'
            message = (
                 f"Hi {request.user.first_name},\n\n"
                 f"Your test drive has been successfully booked with Aurelius Motors.\n\n"
                 f"Booking Details:\n"
                 f"Car: {car.brand} {car.name}\n"
                 f"Date: {date}\n"
                 f"Time: {time}\n\n"
                 f"Please arrive 10 minutes early and bring your driving license.\n\n"
                 f"We look forward to seeing you!\n\n"
                 f"Best regards,\n"
                 f"Aurelius Motors Team"
                )
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [request.user.email],
                fail_silently=False,
            )
            
            messages.success(request, "Test drive booked successfully!")
            return redirect('user_home')

    return render(request, 'user/book_test_drive.html', {'cars': cars})

@login_required
def profile_view(request):
    user = request.user
    return render(request, 'user/profile.html', {'user_data': user})