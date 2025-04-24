from django.urls import path
from .import views
from accounts.views import logout_fn

urlpatterns = [
    path('', views.user_home, name='user_home'),
    path('car/<int:car_id>/', views.car_detail, name='car_detail'),
    path('orders/', views.my_orders, name='my_orders'),
    path('test-drive/', views.book_test_drive, name='book_test_drive'),
    path('service-status/', views.service_status, name='service_status'),
    path('profile/', views.profile_view, name='profile_view'),

    path('logout/', logout_fn, name='logout_fn')
]
