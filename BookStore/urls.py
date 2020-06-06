from django.contrib import admin
from django.urls import path, include
from django.conf import settings # new
from django.conf.urls.static import static

urlpatterns = [
    # Admin url
    path('admin/', admin.site.urls),

    # Local Apps
    path('', include('pages.urls')),
    path('accounts/', include('users.urls')),

    # User management
    path('accounts/', include('allauth.urls')),
    path('books/', include('books.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
