from django.contrib import admin

from django.contrib import admin
from django.shortcuts import redirect, render
from django.urls import path, reverse
from django.utils.html import format_html

from clientes.models import Equipamento

from .models import Servico, TipoAtividade, Atividade
    
    

class AtividadeInline(admin.StackedInline):
    model = Atividade
    extra = 0
    fields = ['tipo_atividade', 'previsao_finalizacao', 'vencimento', 'responsavel']

class ServicoAdmin(admin.ModelAdmin):
    fields = ["cliente", "data_solicitação", "previsao_finalizacao", "vencimento", "solicitado_por", "procurar_por"]
    inlines = [AtividadeInline]
    list_display = ('detail_link', 'status', 'cliente', 'previsao_finalizacao', 'vencimento', 'data_solicitação', 'created_at', 'created_by', 'edit_link', 'delete_link')
    list_filter = ["created_at", "created_by", "status"]
    search_fields = ["cliente", "vencimento"]

    def edit_link(self, obj):
        url = reverse('admin:servicos_servico_change', args=[obj.pk])
        return format_html('<a class="button" href="{}"><i class="fas fa-edit"></i></a>', url)
    edit_link.short_description = 'Editar'
    edit_link.allow_tags = True

    def delete_link(self, obj):
        return format_html('<a class="button" href="{}"><i class="fas fa-trash-alt"></i></a>', reverse('admin:servicos_servico_delete', args=[obj.pk]))
    delete_link.short_description = 'Excluir'
    delete_link.allow_tags = True
    
    
    def detail_link(self, obj):
        url = reverse('admin:servicos_servico_detail', args=[obj.pk])
        return format_html('<a class="button" href="{}"><i class="fas fa-tasks"></i></a>', url)
    detail_link.short_description = 'Detalhes'
    detail_link.allow_tags = True

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path(
                '<path:object_id>/detail/',
                self.admin_site.admin_view(self.detail_view),
                name='servicos_servico_detail',
            ),
        ]
        return custom_urls + urls

    def detail_view(self, request, object_id, form_url='', extra_context=None):
        servico = self.get_object(request, object_id)
        context = dict(
            self.admin_site.each_context(request),
            servico=servico,
        )
        return render(request, 'admin/servicos/detail.html', context)

class TipoAtividadeAdmin(admin.ModelAdmin):
    fields = ["nome", "link_form_base"]
    list_display = ["nome", "link_form_base", "created_at", "created_by"]
    list_filter = ["created_at", "created_by"]
    search_fields = ["nome"]
    
 
admin.site.register(Servico, ServicoAdmin)
admin.site.register(TipoAtividade, TipoAtividadeAdmin)