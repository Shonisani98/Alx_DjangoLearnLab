from django.contrib import admin
from django.urls import path, include
from blog import views  # Make sure this import is present

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
]
