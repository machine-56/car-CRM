from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('user/', include('user.urls')),
    path('ad/', include('admin_panel.urls')),
]
