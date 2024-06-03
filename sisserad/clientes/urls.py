from django.urls import path
from . import views


app_name = "clientes"
urlpatterns = [
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:cliente_id>/equipamento/new/", views.cliente_equipamento_form, name="equipamento-form"),
    path("<int:cliente_id>/endereco/new/", views.cliente_endereco_form, name="endereco-form"),
    path("", views.ListView.as_view(), name="list"),

]