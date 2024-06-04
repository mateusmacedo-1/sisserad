from django.db import models
from django.contrib.auth.models import User

from core.models import BaseModel
STATUS_CHOICES = [
        ('AB', 'Aberto'),
        ('FI', 'Finalizado'),
        ('RE', 'Revisado'),
        ('PU', 'Publicado'),
]
class Servico(BaseModel):
    cliente = models.ForeignKey('clientes.Cliente', on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='AB')
    previsao_finalizacao = models.DateField()
    vencimento = models.DateField()
    data_solicitação = models.DateField()
    
    def __str__(self):
        return f'{self.cliente.nome}'

class TipoAtividade(BaseModel):
    nome = models.CharField(max_length=50)
    link_form_base = models.URLField()
    
    def __str__(self):
        return self.nome
    
class Atividade(BaseModel):
    tipo_atividade = models.ForeignKey(TipoAtividade, on_delete=models.DO_NOTHING)
    equipamento = models.ForeignKey('clientes.Equipamento', on_delete=models.DO_NOTHING)
    previsao_finalizacao = models.DateField()
    vencimento = models.DateField()
    responsavel = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='AB')
    link_formulario = models.URLField()
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    relatorio = models.URLField()
    def __str__(self):
        return f'{self.tipo_atividade.nome} - {self.equipamento.nome}'
    


    