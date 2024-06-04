from os import path
from django.contrib import admin

from .models import Cliente, Endereco, Equipamento
    
    
    
class EnderecoInline(admin.TabularInline):
    model = Endereco
    extra = 0
    fields = ['cep', 'logradouro', 'numero',  'cidade', 'estado']
    
class EquipamentoInline(admin.StackedInline):
    model = Equipamento
    extra = 0
    fields = ['nome', 'fabricante', 'modelo', 'numero_serie', 'ano_fabricacao', 'parametros_variaveis', 'endereco']
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "endereco":
            if 'object_id' in request.resolver_match.kwargs:
                cliente_id = request.resolver_match.kwargs['object_id']
                kwargs["queryset"] = Endereco.objects.filter(cliente_id=cliente_id)
            else:
                kwargs["queryset"] = Endereco.objects.none()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
class ClienteAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["nome", "documento"]}),
        ("Contato", {"fields": ["email", "celular", "telefone_fixo"]}),
    ]
    inlines = [EnderecoInline, EquipamentoInline]
    list_display = ["nome", "documento","created_at"]
    list_filter = ["created_at"]
    search_fields = ["nome", "documento"]
 
admin.site.register(Cliente, ClienteAdmin)