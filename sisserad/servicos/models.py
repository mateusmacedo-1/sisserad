from django.db import models

from core.models import BaseModel
from sisserad import settings

class Servico(BaseModel):
    STATUS_CHOICES = [
        ('AB', 'Aberto'),
        ('FI', 'Finalizado'),
        ('RE', 'Revisado'),
        ('PU', 'Publicado'),
    ]
    cliente = models.ForeignKey('clientes.Cliente', on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='AB')
    previsao_finalizacao = models.DateField()
    vencimento = models.DateField()
    data_solicitação = models.DateField()
    solicitado_por = models.CharField(max_length=50, null=True, blank=True)
    procurar_por = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return f'{self.cliente.nome}'

class TipoAtividade(BaseModel):
    nome = models.CharField(max_length=50)
    link_form_base = models.URLField()
    
    def __str__(self):
        return self.nome
    
class Atividade(BaseModel):
    STATUS_CHOICES = [
        ('AB', 'Aberto'),
        ('FI', 'Finalizado'),
        ('RE', 'Revisado'),
        ('PU', 'Publicado'),
    ]
    tipo_atividade = models.ForeignKey(TipoAtividade, on_delete=models.DO_NOTHING)
    equipamento = models.ForeignKey('clientes.Equipamento', on_delete=models.DO_NOTHING, null=True, blank=True)
    previsao_finalizacao = models.DateField()
    vencimento = models.DateField()
    responsavel = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='AB')
    link_formulario = models.URLField()
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    relatorio = models.URLField()
    revisado_por = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='revisado_por')
    
    def __str__(self):
        return f'{self.tipo_atividade.nome}'

    class Meta:
        permissions = (('pode_revisar', 'Pode revisar uma atividade'),
                        ('pode_publicar', 'Pode publicar uma atividade'),
                        ('pode_visualizar_planilha', 'Permite visualizar a planilha de atividades.'),
                        ('pode_visualizar_laudo', 'Permite visualizar o laudo da atividades.'),
                        ('pode_cancelar_atividade', 'Permite cancelar a atividade.'),
                        ('pode_gerar_retorno', 'Permite gerar atividade de retorno.'),
                    )
    


    