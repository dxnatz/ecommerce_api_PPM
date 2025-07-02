from django.contrib import admin
from django.urls import path, include
from shop.views import index

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('api/', include('shop.urls')),
    path('api/users/', include('users.urls')),  # UNA sola volta
]
