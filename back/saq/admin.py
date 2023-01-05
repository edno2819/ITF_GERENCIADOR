from django.contrib import admin
from saq.models import *


@admin.register(DigitacaoProblema)
class DigitacaoProblemaAdmin(admin.ModelAdmin):
    list_display = ["item", "area", "nome"]
    search_fields = ["item", "area", "nome"]

    class Meta:
        model = DigitacaoProblema


@admin.register(SugestaoMelhora)
class SugestaoMelhoraAdmin(admin.ModelAdmin):
    list_display = ["nome", "id_ambev", "area", "contribuicao"]
    search_fields = ["area", "nome", "id_ambev"]

    class Meta:
        model = SugestaoMelhora


@admin.register(Apresentacao)
class ApresentacaoAdmin(admin.ModelAdmin):
    list_display = ["nome"]
    search_fields = ["nome"]

    class Meta:
        model = Apresentacao
