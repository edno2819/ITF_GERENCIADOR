from django.shortcuts import render
from treinamento.models import Aula

def Treinamento(request, id_aula):
    if request.method == "GET":
        aula = Aula.objects.filter(id=id_aula)[0]
        return render(request, "treinamento.html", {"aula": aula})

def gravarTela(request):
        return render(request, "gravarTela.html")

