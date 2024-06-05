from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from clientes.models import Cliente, Endereco, Equipamento
from clientes.forms import ClienteForm, EnderecoForm, EquipamentoForm
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

class CreateView(generic.CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "clientes/form.html"
    success_url = "clientes:list"
    
    def get_success_url(self):
        return reverse("clientes:detail", args=(self.object.id,))
    
    
class UpdateView(generic.UpdateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "clientes/form.html"

    def get_success_url(self):
        return reverse("clientes:detail", args=(self.object.id,))

class EnderecoUpdateView(generic.UpdateView):
    model = Endereco
    form_class = EnderecoForm
    template_name = "clientes/enderecos/form.html"

    def get_success_url(self):
        return reverse("clientes:detail", args=(self.object.cliente.id,))
    
class EquipamentoUpdateView(generic.UpdateView):
    model = Equipamento
    form_class = EquipamentoForm
    template_name = "clientes/equipamentos/form.html"

    def get_success_url(self):
        return reverse("clientes:detail", args=(self.object.cliente.id,))
    

def cliente_equipamento_form(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    if request.method == "POST":
        form = EquipamentoForm(request.POST, cliente=cliente)
        if form.is_valid():
            form.save()
            return redirect("clientes:detail", pk=cliente_id)
    else:
        form = EquipamentoForm(cliente=cliente)
    return render(request, "clientes/equipamentos/form.html", {
        "cliente": cliente,
        "form": form,
    })
    
def cliente_endereco_form(request, cliente_id):
    cliente = get_object_or_404(Cliente, pk=cliente_id)
    if request.method == "POST":
        form = EnderecoForm(request.POST, cliente=cliente)
        if form.is_valid():
            form.save()
            return redirect("clientes:detail", pk=cliente_id)
    else:
        form = EnderecoForm(cliente=cliente)
    return render(request, "clientes/enderecos/form.html", {
        "cliente": cliente,
        "form": form,
    })

