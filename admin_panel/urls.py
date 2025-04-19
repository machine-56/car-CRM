from django.urls import path
from .import views

urlpatterns = [
    path('', views.adindex, name='adindex'),
    path('car/', views.view_all_cars, name='view_all_cars'),
    path('edit/<int:id>/', views.edit_car, name='edit_car'),
]
