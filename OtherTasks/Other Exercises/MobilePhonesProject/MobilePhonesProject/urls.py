"""
URL configuration for MobilePhonesProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from phone_app.views import index,create,edit,detail,delete
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name='index'),
    path('index/', index, name='index'),
    path('newProduct/create/', create, name='create'),
    path('product/<phone_id>/', detail, name='detail'),
    path('product/edit/<phone_id>/', edit, name='edit'),
    path('product/delete/<phone_id>/', delete, name='delete'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
