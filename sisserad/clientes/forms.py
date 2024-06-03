from django import forms

from clientes.models import Cliente, Endereco, Equipamento


class EquipamentoForm(forms.ModelForm):
    class Meta:
        model = Equipamento
        fields = ["nome", "fabricante", "modelo", "numero_serie", "ano_fabricacao", "parametros_variaveis", "endereco"]
    def __init__(self, *args, **kwargs):
        cliente_id = kwargs.pop('cliente_id', None)
        self.cliente = Cliente.objects.get(pk=cliente_id)
        super(EquipamentoForm, self).__init__(*args, **kwargs)
        if self.cliente:
            self.fields['endereco'].queryset = self.cliente.endereco_set.all()
    def save(self, commit=True):
        equipamento = super(EquipamentoForm, self).save(commit=False)
        if self.cliente:
            equipamento.cliente = self.cliente
        if commit:
            equipamento.save()
        return equipamento    
        

class EnderecoForm(forms.ModelForm):
    class Meta:
        model = Endereco
        fields = ['logradouro', 'numero', 'cep', 'cidade', 'estado']
    def __init__(self, *args, **kwargs):
        self.cliente = kwargs.pop('cliente', None)
        super(EnderecoForm, self).__init__(*args, **kwargs)

        
    def save(self, commit=True):
        endereco = super(EnderecoForm, self).save(commit=False)
        if self.cliente:
            endereco.cliente = self.cliente
        if commit:
            endereco.save()
        return endereco 
    
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ["nome", "documento", "email", "telefone_fixo", "celular"]
