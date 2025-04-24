from django.contrib import admin
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('user/', include('user.urls')),
    path('ad/', include('admin_panel.urls')),
    path('sales/', include('sales_dpt.urls')),
    path('telecaller/', include('telecaller_dpt.urls')),
    path('service/', include('service_dpt.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
