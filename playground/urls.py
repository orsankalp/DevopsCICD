from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('booking/', views.booking, name='booking'),
    path('cars/', views.cars, name='cars'),
    path('contact/', views.contact, name='contact'),
    path('category/', views.category, name='category'),
    path('help/', views.help, name='Help'),
]