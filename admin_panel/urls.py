from django.urls import path
from .import views
from accounts.views import logout_fn

urlpatterns = [
    path('', views.admin_home, name='admin_home'),
    path('car/', views.view_all_cars, name='view_all_cars'),
    path('edit/<int:id>/', views.edit_car, name='edit_car'),
    path('performance/', views.showroom_performance, name='showroom_performance'),

    path('logout/', logout_fn, name='logout_fn')
]
