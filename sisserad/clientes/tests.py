from django.db import IntegrityError
from django.test import TestCase

from clientes.models import Cliente

from django.core.exceptions import (
    ValidationError,
)


# Create your tests here.
class ClienteModelTest(TestCase):
    def test_somente_um_cliente_por_documento(self):
        Cliente.objects.create(nome="João", documento="12345678901", email="joao@gmail.com", celular="999999999")
        with self.assertRaises(IntegrityError):
            Cliente.objects.create(nome="Maria", documento="12345678901", email="jose@gmail.com", celular="999999999")
    def test_somente_um_cliente_por_email(self):
        Cliente.objects.create(nome="João", documento="12345678901", email="joao@gmail.com", celular="999999999")
        with self.assertRaises(IntegrityError):
            Cliente.objects.create(nome="Maria", documento="123555221", email="joao@gmail.com", celular="999999999")
class EnderecoModelTest(TestCase):
    """
        A unicidade do endereço é testada com uma combinação de cep e número.
    """
    def test_endereco_deve_ser_unico_por_cliente(self):
        c = Cliente.objects.create(nome="Maria", documento="123555221", email="joao@gmail.com", celular="999999999")
        c.endereco_set.create(logradouro="Rua 1", numero="123", cep="12345678", cidade="mossoro", estado="rn")
        with self.assertRaises(ValidationError):
            c.endereco_set.create(logradouro="Rua 2", numero="123", cep="12345678", cidade="mossoro", estado="rn")
        