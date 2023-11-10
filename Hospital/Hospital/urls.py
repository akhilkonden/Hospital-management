from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static  # Import the static function
from django.conf import settings  # Import the settings module

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('booking.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
