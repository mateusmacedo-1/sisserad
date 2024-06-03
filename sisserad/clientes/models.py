from django.db import models
from core.models import BaseModel
from django.core.exceptions import (
    ValidationError,
)
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
    parametros_variaveis = models.CharField(max_length=255, null=True, blank=True)
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    ativo = models.BooleanField(default=True)
    endereco = models.ForeignKey('Endereco', on_delete=models.SET_NULL, blank=True, null=True)
    
    def clean(self, *args, **kwargs):
        if self.cliente.equipamento_set.filter(numero_serie=self.numero_serie).exists():
            raise ValidationError('Equipamento já cadastrado para este cliente')
        super().clean(*args, **kwargs)
    
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f'{self.nome} Nº Série: {self.numero_serie}'

class Endereco(BaseModel):
    id = models.AutoField(primary_key=True, editable=False, unique=True)
    logradouro = models.CharField(max_length=255)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=255, null=True, blank=True)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=10)
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    ativo = models.BooleanField(default=True)

    def clean(self, *args, **kwargs):
        if self.cliente.endereco_set.filter(cep=self.cep, numero=self.numero).exists():
            raise ValidationError('Endereço já cadastrado para este cliente')
        super().clean(*args, **kwargs)
        
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.logradouro}, {self.numero} CEP:{self.cep}'