from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Admin url
    path('anything-but-admin/', admin.site.urls),

    # Local Apps
    path('', include('pages.urls')),
    path('accounts/', include('users.urls')),

    # User management
    path('accounts/', include('allauth.urls')),
    path('books/', include('books.urls')),
    path('orders/', include('orders.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns