from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('masters/', include('masters.urls')),
    path('authentication/', include('authentication.urls')),
    path('labour_management/', include('labour_management.urls')), 
    path('clients/', include('client.urls')), 
    path('project/', include('project.urls')), 
]
