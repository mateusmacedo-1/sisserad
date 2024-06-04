from django.urls import path
from . import views


app_name = "clientes"
urlpatterns = [
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:cliente_id>/equipamento/new/", views.cliente_equipamento_form, name="equipamento-form"),
    path("<int:cliente_id>/equipamento/<int:pk>/edit/", views.EquipamentoUpdateView.as_view(), name="equipamento-editar"),
    path("<int:cliente_id>/endereco/new/", views.cliente_endereco_form, name="endereco-form"),
    path("<int:cliente_id>/endereco/<int:pk>/edit/", views.EnderecoUpdateView.as_view(), name="endereco-editar"),
    path("", views.ListView.as_view(), name="list"),
    path("new/", views.CreateView.as_view(), name="create"),
    path("<int:pk>/edit/", views.UpdateView.as_view(), name="editar"),

]