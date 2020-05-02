from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # admin
    path('accounts/', include('django.contrib.auth.urls')),  # user management
    path('accounts/', include('users.urls')),  # new
    path('', include('pages.urls')),  # local
]
