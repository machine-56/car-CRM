from django.urls import path
from .import views
from accounts.views import logout_fn

urlpatterns = [
    path('', views.finance_home, name='finance_home'),
    path('staff-salary/', views.staff_salary, name='staff_salary'),
    path('staff-attendance/', views.staff_attendance, name='staff_attendance'),
    
    path('logout/', logout_fn, name='logout_fn')
]