from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("/appointment", include("appointments.urls")),
    path("admin/", admin.site.urls),
]
