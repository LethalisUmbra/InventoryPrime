from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('inventory.urls')),
    path('Primary/', include('primary.urls')),
    path('primary/', include('primary.urls')),
]