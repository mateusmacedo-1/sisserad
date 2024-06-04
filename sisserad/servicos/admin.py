from django.contrib import admin

from django.contrib import admin

from .models import Servico, TipoAtividade, Atividade
    
    

    
class ServicoAdmin(admin.ModelAdmin):
    fields = ["cliente", "data_solicitação", "previsao_finalizacao", "vencimento", ]
    list_display = ["cliente", "previsao_finalizacao", "vencimento", "data_solicitação", "created_at", "created_by"]
    list_filter = ["created_at", "created_by"]
    search_fields = ["cliente", "vencimento"]
 
admin.site.register(Servico, ServicoAdmin)