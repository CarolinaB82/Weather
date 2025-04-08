from django.urls import path
from . import views

urlpatterns = [
    # URL qui accepte un paramètre "city"
    path('api/weather/<str:city>/', views.weather, name='weather'),
]
