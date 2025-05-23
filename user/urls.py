from django.urls import path
from .import views
from accounts.views import logout_fn

urlpatterns = [
    path('', views.user_home, name='user_home'),
    path('car/<int:car_id>/', views.car_detail, name='car_detail'),
    path('orders/', views.my_orders, name='my_orders'),
    path('test-drive/', views.book_test_drive, name='book_test_drive'),
    path('service-status/', views.service_status, name='service_status'),
    path('service-status/view/', views.status_view, name='status_view'),
    path('profile/', views.profile_view, name='profile_view'),
    path('vehicle/countdown/', views.view_vehicle_countdown, name='view_vehicle_countdown'),

    path('logout/', logout_fn, name='logout_fn')
]
