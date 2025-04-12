"""
URL configuration for meteo_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
#from django.contrib import admin
#from django.urls import path
#from weather import views  # On importe directement les vues depuis weather

#urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('api/weather/', views.weather),  # Appel de la vue weather directement depuis weather
#]

# meteo_project/urls.py
#from django.contrib import admin
#from django.urls import path, include  # 'include' permet d'inclure d'autres fichiers d'URLs

#urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('api/', include('weather.urls')),  # Inclut les URLs de l'application 'weather'
#]
# meteo_project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('weather.urls')),  # Inclure les URLs de l'app weather
]