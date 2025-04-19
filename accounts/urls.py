from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_fn, name='login_fn'),
    path('logout_fn/', views.logout_fn, name='logout_fn'),
    path('register/', views.register_fn, name='register_fn'),

    
    path("validate/", views.validate_field, name="validate_field"),

]
