from django.contrib import admin
from django.urls import path, include
from XEC import views

urlpatterns = [
    path('', views.AysHome, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),

]
