from django.shortcuts import get_object_or_404, redirect, render
from clientes.models import Cliente
from clientes.forms import EnderecoForm, EquipamentoForm
from django.views import generic


class DetailView(generic.DetailView):
    model = Cliente
    template_name = "clientes/detail.html"

class ListView(generic.ListView):
    model = Cliente
    template_name = "clientes/list.html"
    context_object_name = "latest_registered_clientes"
    
    def get_queryset(self):
        return Cliente.objects.order_by("-created_at")[:5]

def cliente_equipamento_form(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    if request.method == "POST":
        form = EquipamentoForm(request.POST, cliente_id=cliente_id)
        if form.is_valid():
            form.save()
            return redirect("clientes:detail", cliente_id=cliente_id)
    else:
        form = EquipamentoForm(cliente_id=cliente.id)
    return render(request, "clientes/equipamentos/form.html", {
        "cliente": cliente,
        "form": form,
    })
    
def cliente_endereco_form(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    if request.method == "POST":
        form = EnderecoForm(request.POST, cliente_id=cliente_id)
        if form.is_valid():
            form.save()
            return redirect("clientes:detail", cliente_id=cliente_id)
    else:
        form = EnderecoForm(cliente_id=cliente.id)
    return render(request, "clientes/enderecos/form.html", {
        "cliente": cliente,
        "form": form,
    })

