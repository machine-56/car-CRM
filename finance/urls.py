from django.urls import path
from . import views
from accounts.views import logout_fn

urlpatterns = [
    path('', views.finance_home, name='finance_home'),
    path('staff-salary/', views.staff_salary, name='staff_salary'),
    path('staff-attendance/', views.staff_attendance, name='staff_attendance'),
    path('sales/', views.sales_page, name='sales_page'),
    path('spare-parts/', views.spare_parts, name='spare_parts'),
    path('spare-parts-orders/', views.spare_parts_orders, name='spare_parts_orders'),

    path('service/history/', views.service_history, name='service_history'),
    path('service/detail/<int:token>/', views.service_detail, name='service_detail'),
    path('service/payment/<int:token>/', views.service_payment, name='service_payment'),
    path('service/print_token/<int:token>/', views.print_token, name='print_token'),
    path('service/print_bill/<int:token>/', views.print_bill, name='print_bill'),

    path('service/set_countdown/', views.set_countdown, name='set_countdown'),


    path('logout/', logout_fn, name='logout_fn'),
]
