from django.urls import path
from .import views
from accounts.views import login_fn

urlpatterns = [
    path('', views.user_home, name='user_home'),

    path('logout/', login_fn, name='logout_fn')
]
