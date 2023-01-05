from django.urls import path
from saq.views import *

urlpatterns = [
    #formularios
    path("form/soda", FormSaq, name="soda"),
    path("form/sugestao", FormSugestao, name="sugestao"),
    path("teste", teste, name="teste"),
    
    #soda
    path("soda", soda, name="soda"),
    path("coletas", coletas, name="coletas"),
    
    #apresentação
    path("apresentacoes", apresentacoes, name="coletas"),
    path("apresentacoes/", apresentacao, name="coletas"),
]
