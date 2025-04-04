from django.shortcuts import render
from .models import Medico, Consulta
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .forms import ConsultaForm, MedicoForm
from .serializers import MedicoSerializer, ConsultaSerializer
from rest_framework import status


#inicio das aplicações

#mostra médicos
@api_view(['GET'])
def listar_medicos(resquest):
    medicos = Medico.objects.filter()
    serializer = MedicoSerializer(medicos, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def criar_medico(request):
    if request.method == 'POST':
        forms = MedicoForm(data=request.data)
        if forms.is_valid():
           medico =  forms.save()
           serializer = MedicoSerializer(medico)
           return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(forms.errors, status=status.HTTP_400_BAD_REQUEST)

#resgistra consultas
@api_view(['POST'])
def criar_consulta(request):
    if request.method == 'POST':
        forms = ConsultaForm(data=request.data)
        if forms.is_valid():
           consulta =  forms.save()
           serializer = ConsultaSerializer(consulta)
           return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(forms.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET'])
def detalhes_consulta(request, pk):
    try:
        consulta = Consulta.objects.get(pk = pk)
    except Consulta.DoesNotExist:
        return Response({"erro": "essa consulta nao existe"}, status=status.HTTP_404_NOT_FOUND)
    forms = ConsultaForm(consulta)
    return Response(forms.data)