from django.db import models
from core.models import BaseModel

class Cliente(BaseModel):
    id = models.AutoField(primary_key=True, editable=False, unique=True)
    nome = models.CharField(max_length=255, blank=False, null=False)
    documento = models.CharField(max_length=50, blank=False, null=False, unique=True)
    email = models.EmailField(max_length=50, blank=False, null=False, unique=True)
    telefone_fixo = models.CharField(max_length=20, blank=True, null=True)
    celular = models.CharField(max_length=20)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.nome.capitalize()}(Documento: {self.documento})'

class Equipamento(BaseModel):
    id = models.AutoField(primary_key=True, editable=False, unique=True)
    nome = models.CharField(max_length=255)
    fabricante = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    numero_serie = models.CharField(max_length=50)
    ano_fabricacao = models.IntegerField()
    parametros_variaveis = models.CharField(max_length=255)
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    ativo = models.BooleanField(default=True)
    endereco = models.ForeignKey('Endereco', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'{self.nome} Nº Série: {self.numero_serie}'

class Endereco(BaseModel):
    id = models.AutoField(primary_key=True, editable=False, unique=True)
    logradouro = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=255)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=10)
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    ativo = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.logradouro}, {self.numero} CEP:{self.cep}'