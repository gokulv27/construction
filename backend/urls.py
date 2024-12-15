from django.contrib import admin
from django.urls import path,include

urlpatterns =[
    path('admin/', admin.site.urls),
    path('api/account/',include ('accounts.urls')),
    path('api/master/',include('master.urls') ),
    path('api/labour/', include('labour_management.urls') ),
    path('api/client/', include('client.urls') ),
    path('api/project/',include('project.urls')),
]

