"""
URL configuration for sisserad project.

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
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from servicos import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='admin/')),
    path("clientes/", include("clientes.urls")),
    path('servicos/', include('servicos.urls', namespace='servicos')),
    path("api/atividades/<int:pk>/abrir/", views.AbrirAtividade.as_view(), name="abrir_atividade"),
    path("api/atividades/<int:pk>/finalizar/", views.FinalizarAtividade.as_view(), name="finalizar_atividade"),
    path("api/atividades/<int:pk>/revisar/", views.RevisarAtividade.as_view(), name="revisar_atividade"),
    path("api/atividades/<int:pk>/publicar/", views.PublicarAtividade.as_view(), name="publicar_atividade"),
]
