
from django.contrib import admin
from django.urls import path, include
 



urlpatterns = [
    path("first_app/", include("first_app.urls")),
    path('admin/', admin.site.urls),
]
