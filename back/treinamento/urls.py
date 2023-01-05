from django.urls import path
from treinamento.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("aula/<str:id_aula>", login_required(Treinamento), name="aula"),
    path("gravar", gravarTela, name="gravarAula"),
]
