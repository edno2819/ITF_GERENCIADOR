from django.shortcuts import render
from .forms import *
from tarefas.models import Soda

def FormSaq(request):
    if request.method == "GET":
        form = SaqMesDigitacao()
        return render(request, "MesDigitacao.html", {"form": form})
    else:
        form = SaqMesDigitacao(request.POST)
        if form.is_valid():
            saq = form.save()
            form = SaqMesDigitacao()
        return render(request, "MesDigitacao.html", {"form": form, "resultado": True})


def FormSugestao(request):
    if request.method == "GET":
        form = SugestaoMelhoraForm()
        return render(request, "SugestaoMelhoraForm.html", {"form": form})
    else:
        form = SugestaoMelhoraForm(request.POST)
        if form.is_valid():
            saq = form.save()
            form = SugestaoMelhoraForm()
        return render(
            request, "SugestaoMelhoraForm.html", {"form": form, "resultado": True}
        )


def teste(request):
    return render(request, "teste.html")


def soda(request):
    return render(request, "sodaExplicacao.html")


def coletas(request):
    itens_por_areas = {}
    teste = list(Soda.objects.filter(status="OK").values("area", "nome"))

    c = 0
    for item in teste:
        c += 1
        if item["area"] not in itens_por_areas:
            itens_por_areas[item["area"]] = {"id": f"key{c}", "value": []}
        itens_por_areas[item["area"]]["value"].append(item["nome"])

    return render(
        request, "coletaAutomatica.html", {"itens_por_areas": itens_por_areas}
    )

def apresentacoes(request):
    return render(request, "apresentacoes.html")

def apresentacao(request):
    return render(request, "apresentacoes.html")


