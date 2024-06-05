from django.views import generic

from servicos.models import Atividade, Servico

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

class DetailView(generic.DetailView):
    model = Servico
    template_name = "servicos/detail.html"
    
class AbrirAtividade(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, pk):
        try:
            atividade = Atividade.objects.get(pk=pk)
        except Atividade.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if (atividade.status == 'AB'):
            return Response(status=status.HTTP_409_CONFLICT, data={'message': 'Atividade já está aberta'})
        atividade.status = 'AB'
        atividade.save()
        return Response(status=status.HTTP_200_OK)
class FinalizarAtividade(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, pk):
        try:
            atividade = Atividade.objects.get(pk=pk)
        except Atividade.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if (atividade.status != 'AB'):
            return Response(status=status.HTTP_409_CONFLICT, data={'message': 'Atividade deve estar aberta para ser finalizada.'})
        atividade.status = 'FI'
        atividade.save()
        return Response(status=status.HTTP_200_OK)

class RevisarAtividade(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, pk):
        try:
            atividade = Atividade.objects.get(pk=pk)
        except Atividade.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if (atividade.status != 'FI'):
            return Response(status=status.HTTP_409_CONFLICT, data={'message': 'Atividade deve estar finalizada para ser revisada.'})
        atividade.status = 'RE'
        atividade.save()
        return Response(status=status.HTTP_200_OK)

class PublicarAtividade(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, pk):
        try:
            atividade = Atividade.objects.get(pk=pk)
        except Atividade.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        if (atividade.status != 'RE'):
            return Response(status=status.HTTP_409_CONFLICT, data={'message': 'Atividade deve estar revisada para ser publicada.'})
        atividade.status = 'PU'
        atividade.save()
        return Response(status=status.HTTP_200_OK)