from django.shortcuts import get_object_or_404, redirect, render
from clientes.models import Cliente
from clientes.forms import EquipamentoForm


# Create your views here.
def cliente_list(request):
    latest_registered_clientes = Cliente.objects.order_by("-created_at")[:5]
    context = {
        "latest_registered_clientes": latest_registered_clientes,
    }
    return render(request, "clientes/list.html", context)

def cliente_detail(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    context = {
        "cliente": cliente,
    }
    return render(request, "clientes/detail.html", context)

def cliente_equipamento_form(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    if request.method == "POST":
        form = EquipamentoForm(request.POST, cliente_id=cliente_id)
        if form.is_valid():
            form.instance.cliente = cliente
            form.save()
            return redirect("clientes:detail", cliente_id=cliente_id)
    else:
        form = EquipamentoForm(cliente_id=cliente.id)
    return render(request, "clientes/equipamentos/form.html", {
        "cliente": cliente,
        "form": form,
    })

