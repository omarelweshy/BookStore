from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Admin url
    path('admin/', admin.site.urls),

    # Local Apps
    path('', include('pages.urls')),
    path('accounts/', include('users.urls')),

    # User management
    path('accounts/', include('allauth.urls')),

]
