from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/masters/', include('masters.urls')),
    path('authentication/', include('authentication.urls')),
    path('labour_management/', include('labour_management.urls')), 
    path('clients/', include('client.urls')), 
    path('project/', include('project.urls')), 
]

# Serve media files during development
if settings.DEBUG:  
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
