from django.urls import path
from . import views


app_name = "clientes"
urlpatterns = [
    path("/<int:cliente_id>/", views.cliente_detail, name="detail"),
    path("/<int:cliente_id>/equipamento/new", views.cliente_equipamento_form, name="equipamento-form"),
    path("", views.cliente_list, name="list"),

]