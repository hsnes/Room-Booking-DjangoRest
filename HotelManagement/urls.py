"""HotelManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from HotelManagement import settings
from .views import book_list

urlpatterns = [
    path('books', book_list),
    path('api/', include('reservation.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    '''add root static files'''
    urlpatterns = urlpatterns + static(settings.STATIC_URL, doument_root=settings.STATIC_ROOT)
