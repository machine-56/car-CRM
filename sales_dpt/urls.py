from django.urls import path
from .import views
from accounts.views import logout_fn

urlpatterns = [
    path('', views.sales_home, name='sales_home'),
    path('add/customers/', views.upload_customers, name='upload_customers'),
    path('customers/', views.view_customer, name='view_customer'),
    path('orders/', views.order_list, name='order_list'),
    path('stocks/', views.stocks, name='stocks'),
    path('staffs/', views.staffs, name='staffs'),
    path('staff_profile/<int:id>/', views.staff_profile, name='staff_profile'),
    path('telecaller_home/', views.telecaller_home, name='telecaller_home'),

    path('logout/', logout_fn, name='logout_fn')

]