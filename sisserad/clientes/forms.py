from django import forms

from clientes.models import Cliente, Equipamento


class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields = ["nome", "fabricante", "modelo", "numero_serie", "ano_fabricacao", "parametros_variaveis", "endereco"]
    def __init__(self, *args, **kwargs):
        self.cliente_id = kwargs.pop('cliente_id', None)
        super(EquipamentoForm, self).__init__(*args, **kwargs)
        if self.cliente_id:
            cliente = Cliente.objects.get(pk=self.cliente_id)
            self.fields['endereco'].queryset = cliente.endereco_set.all()