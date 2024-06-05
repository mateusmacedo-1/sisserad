from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Atividade, TipoAtividade, Servico
from clientes.models import Cliente, Equipamento, Endereco

class AtividadeAPITestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)

        self.cliente = Cliente.objects.create(
            nome='Cliente Teste',
            documento='12345678900',
            email='cliente@teste.com',
            telefone_fixo='123456789',
            celular='987654321'
        )

        self.endereco = Endereco.objects.create(
            logradouro='Rua Teste',
            numero='123',
            complemento='Apto 1',
            cidade='Cidade Teste',
            estado='TE',
            cep='12345-678',
            cliente=self.cliente
        )

        self.equipamento = Equipamento.objects.create(
            nome='Equipamento Teste',
            fabricante='Fabricante Teste',
            modelo='Modelo Teste',
            numero_serie='123456',
            ano_fabricacao=2022,
            parametros_variaveis='Variáveis Teste',
            cliente=self.cliente,
            endereco=self.endereco
        )

        self.servico = Servico.objects.create(
            cliente=self.cliente,
            previsao_finalizacao='2024-12-31',
            vencimento='2024-12-31',
            data_solicitação='2024-01-01'
        )

        self.tipo_atividade = TipoAtividade.objects.create(
            nome='Tipo Teste',
            link_form_base='http://example.com/form'
        )

        self.atividade = Atividade.objects.create(
            tipo_atividade=self.tipo_atividade,
            equipamento=self.equipamento,
            previsao_finalizacao='2024-12-31',
            vencimento='2024-12-31',
            responsavel=self.user,
            link_formulario='http://example.com',
            servico=self.servico,
            relatorio='http://example.com/report'
        )

    def test_abrir_atividade_nao_encontrada(self):
        response = self.client.post(f'/api/atividades/9999/abrir/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_abrir_atividade_ja_aberta(self):
        response = self.client.post(f'/api/atividades/{self.atividade.pk}/abrir/')
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)
        self.assertEqual(response.data['message'], 'Atividade já está aberta')
    
    def test_abrir_atividade_finalizada(self):
        self.atividade.status = 'FI'
        self.atividade.save()
        response = self.client.post(f'/api/atividades/{self.atividade.pk}/abrir/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.atividade.refresh_from_db()
        self.assertEqual(self.atividade.status, 'AB')
    
    def test_abrir_atividade_revisada(self):
        self.atividade.status = 'RE'
        self.atividade.save()
        response = self.client.post(f'/api/atividades/{self.atividade.pk}/abrir/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.atividade.refresh_from_db()
        self.assertEqual(self.atividade.status, 'AB')
    
    def test_abrir_atividade_publicada(self):
        self.atividade.status = 'PU'
        self.atividade.save()
        response = self.client.post(f'/api/atividades/{self.atividade.pk}/abrir/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.atividade.refresh_from_db()
        self.assertEqual(self.atividade.status, 'AB')
    
    def test_finalizar_atividade_sucesso(self):
        self.atividade.status = 'AB'
        self.atividade.save()
        response = self.client.post(f'/api/atividades/{self.atividade.pk}/finalizar/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.atividade.refresh_from_db()
        self.assertEqual(self.atividade.status, 'FI')

    def test_abrir_atividade_sucesso(self):
        self.atividade.status = 'FI'
        self.atividade.save()
        response = self.client.post(f'/api/atividades/{self.atividade.pk}/abrir/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.atividade.refresh_from_db()
        self.assertEqual(self.atividade.status, 'AB')

    def test_finalizar_atividade_nao_encontrada(self):
        response = self.client.post(f'/api/atividades/9999/finalizar/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_finalizar_atividade_finalizada(self):
        self.atividade.status = 'FI'
        self.atividade.save()
        response = self.client.post(f'/api/atividades/{self.atividade.pk}/finalizar/')
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)
        self.assertEqual(response.data['message'], 'Atividade deve estar aberta para ser finalizada.')
        
    def test_finalizar_atividade_revisada(self):
        self.atividade.status = 'RE'
        self.atividade.save()
        response = self.client.post(f'/api/atividades/{self.atividade.pk}/finalizar/')
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)
        self.assertEqual(response.data['message'], 'Atividade deve estar aberta para ser finalizada.')
        
    def test_finalizar_atividade_publicada(self):
        self.atividade.status = 'PU'
        self.atividade.save()
        response = self.client.post(f'/api/atividades/{self.atividade.pk}/finalizar/')
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)
        self.assertEqual(response.data['message'], 'Atividade deve estar aberta para ser finalizada.')
    
    def test_revisar_atividade_nao_encontrada(self):
        response = self.client.post(f'/api/atividades/9999/revisar/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        
    def test_revisar_atividade_sucesso(self):
        self.atividade.status = 'FI'
        self.atividade.save()
        response = self.client.post(f'/api/atividades/{self.atividade.pk}/revisar/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.atividade.refresh_from_db()
        self.assertEqual(self.atividade.status, 'RE')
    
    def test_revisar_atividade_aberta(self):
        self.atividade.status = 'AB'
        self.atividade.save()
        response = self.client.post(f'/api/atividades/{self.atividade.pk}/revisar/')
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)
        self.assertEqual(response.data['message'], 'Atividade deve estar finalizada para ser revisada.')
        
    def test_revisar_atividade_publicada(self):
        self.atividade.status = 'PU'
        self.atividade.save()
        response = self.client.post(f'/api/atividades/{self.atividade.pk}/revisar/')
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)
        self.assertEqual(response.data['message'], 'Atividade deve estar finalizada para ser revisada.')
    
    def test_revisar_atividade_revisada(self):
        self.atividade.status = 'RE'
        self.atividade.save()
        response = self.client.post(f'/api/atividades/{self.atividade.pk}/revisar/')
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)
        self.assertEqual(response.data['message'], 'Atividade deve estar finalizada para ser revisada.')
    
    def test_publicar_atividade_nao_encontrada(self):
        response = self.client.post(f'/api/atividades/9999/publicar/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_publicar_atividade_sucesso(self):
        self.atividade.status = 'RE'
        self.atividade.save()
        response = self.client.post(f'/api/atividades/{self.atividade.pk}/publicar/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.atividade.refresh_from_db()
        self.assertEqual(self.atividade.status, 'PU')
    
    def test_publicar_atividade_aberta(self):
        self.atividade.status = "AB"
        self.atividade.save()
        response = self.client.post(f'/api/atividades/{self.atividade.pk}/publicar/')
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)
        self.assertEqual(response.data['message'], 'Atividade deve estar revisada para ser publicada.')
        
    def test_publicar_atividade_finalizada(self):
        self.atividade.status = "FI"
        self.atividade.save()
        response = self.client.post(f'/api/atividades/{self.atividade.pk}/publicar/')
        self.assertEqual(response.status_code, status.HTTP_409_CONFLICT)
        self.assertEqual(response.data['message'], 'Atividade deve estar revisada para ser publicada.')



