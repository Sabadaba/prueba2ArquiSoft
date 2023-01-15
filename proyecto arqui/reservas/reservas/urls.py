"""reservas URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from API import views as api_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/estudiantes', api_views.ListaEstudiante.as_view()),
    path('api/estudiantes/<int:id>', api_views.DetalleEstudiante.as_view()),
    path('api/profesores', api_views.ListaProfesor.as_view()),
    path('api/profesores/<int:id>', api_views.DetalleProfesor.as_view()),
    path('api/espacios', api_views.ListaEspacio.as_view()),
    path('api/espacios/<int:id>', api_views.DetalleEspacio.as_view()),
    path('api/reservas', api_views.ListaReserva.as_view()),
    path('api/reservas/<int:id>', api_views.DetalleReserva.as_view())
]
