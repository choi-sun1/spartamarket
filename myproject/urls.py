
from django.contrib import admin
from django.urls import path,include
from products import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('products/', include('products.urls')),
    path('users/', include('users.urls')),
    path('accounts/', include('accounts.urls')),
    ]