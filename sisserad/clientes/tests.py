from django.db import IntegrityError
from django.test import TestCase
from django.urls import reverse

from clientes.models import Cliente

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
        with self.assertRaises(IntegrityError):
            c.endereco_set.create(logradouro="Rua 2", numero="123", cep="12345678", cidade="mossoro", estado="rn")

class ClienteViewTest(TestCase):
    def test_sem_clientes(self):
        """
        Se não existem clientes, uma mensagem apropriada deve ser exibida.
        """
        response = self.client.get(reverse("clientes:list"))
        self.assertContains(response, "Não há clientes disponíveis.")
        self.assertQuerySetEqual(response.context["latest_registered_clientes"], [])
        self.assertEqual(response.status_code, 200)
        
    def test_clientes_details_view_com_endereco(self):
        """
            Os endereços do cliente devem ser exibidos na página de detalhes.
        """
        c = Cliente.objects.create(nome="Maria", documento="123555221", email="mateus@gmail.com", celular="999999999")
        c.endereco_set.create(logradouro="Rua 1", numero="123", cep="12345678", cidade="mossoro", estado="rn")
        c.endereco_set.create(logradouro="Rua 2", numero="123", cep="12312321", cidade="mossoro", estado="rn")
        c.endereco_set.create(logradouro="Rua 3", numero="123", cep="123123121", cidade="mossoro", estado="rn")
        response = self.client.get(reverse("clientes:detail", args=(c.id,)))
        self.assertContains(response, c.endereco_set.all()[0].__str__())
        self.assertContains(response, c.endereco_set.all()[1].__str__())
        self.assertContains(response, c.endereco_set.all()[2].__str__())
        self.assertEqual(response.status_code, 200)
    def test_clientes_details_view_com_equipamento(self):
        """
            Os equipamentos do cliente devem ser exibidos na página de detalhes.
        """
        c = Cliente.objects.create(nome="Maria", documento="123555221", email="mateus@gmail.com", celular="999999999")
        e = c.endereco_set.create(logradouro="Rua 1", numero="123", cep="12345678", cidade="mossoro", estado="rn")
        e.equipamento_set.create(nome="Bomba", fabricante="Bosch", modelo="Bomba de agua", numero_serie="123123", ano_fabricacao=2020, cliente=c)
        e.equipamento_set.create(nome="Bomba", fabricante="Bosch", modelo="Bomba de agua", numero_serie="12356", ano_fabricacao=2020, cliente=c)
        e.equipamento_set.create(nome="Bomba", fabricante="Bosch", modelo="Bomba de agua", numero_serie="126890", ano_fabricacao=2020, cliente=c)
        response = self.client.get(reverse("clientes:detail", args=(c.id,)))
        self.assertContains(response, e.equipamento_set.all()[0].__str__())
        self.assertContains(response, e.equipamento_set.all()[1].__str__())
        self.assertContains(response, e.equipamento_set.all()[2].__str__())
        
    def test_clientes_form_view_erros(self):
        """
            O formulário deve exibir erros se os dados são inválidos.
        """
        c = Cliente.objects.create(nome="Maria", documento="123555221", email="mateus@gmail.com", celular="999999999")
        response = self.client.post(reverse("clientes:edit", 
                                    args=(c.id,)), 
                                    data={"nome": "Maria", "documento": "123555221", "email": "mateusgmail.com", "celular": "999999999"})
        
        
    
        