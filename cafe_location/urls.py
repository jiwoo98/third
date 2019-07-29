from django.contrib import admin
from django.urls import path
import cafe.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', cafe.views.home, name="home"),
]
