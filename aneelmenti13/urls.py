"""
URL configuration for aneelmenti13 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from productsapp.views import ProductsInput,ProductsInsert,ProductsDisplay,ProductsDeleteInput,ProductsDelete,ProductsUpdateInput,ProductsUpdate
urlpatterns = [
    path('admin/', admin.site.urls),
    path('productsapp/',ProductsInput.as_view()),
    path('productsapp/insert',ProductsInsert.as_view()),
    path('productsapp/display',ProductsDisplay.as_view()),
    path('productsapp/deleteinput',ProductsDeleteInput.as_view()),
    path('productsapp/delete',ProductsDelete.as_view()),
    path('productsapp/updateinput',ProductsUpdateInput.as_view()),
    path('productsapp/update',ProductsUpdate.as_view()),
]
