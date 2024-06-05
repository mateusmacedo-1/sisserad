from django.views import generic

from servicos.models import Servico

class DetailView(generic.DetailView):
    model = Servico
    template_name = "servicos/detail.html"