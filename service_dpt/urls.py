from django.urls import path
from .import views
from accounts.views import logout_fn

urlpatterns = [
    path('', views.service_home, name='service_home'),
    path('add/', views.add_service_token, name='add_service_token'),
    path('token/', views.token_view, name='token_view'),
    path('flow/', views.service_flow, name='service_flow'),
    path('staff/', views.staff_performance, name='staff_performance'),
    path('staff/<int:staff_id>/', views.staff_profile, name='staff_profile'),

    path('logout/', logout_fn, name='logout_fn')
]