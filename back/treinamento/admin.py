from django_summernote.admin import SummernoteModelAdmin
from admin_extra_buttons.api import ExtraButtonsMixin, button
from django.shortcuts import redirect
from django.contrib import admin
from treinamento.models import *
from utils.css import *


@admin.register(Aula)
class aulasAdmin(SummernoteModelAdmin, ExtraButtonsMixin, admin.ModelAdmin):
    summernote_fields = "descricao"
    search_fields = ["nome"]
    list_filter = ["nome"]
    list_display = ["nome", "verAula"]

    def verAula(self, obj):
        return format_html(
            """<a  target="_blank" style='{}' href="/treinamento/aula/{}">
            Assistir aula</a>""",
            button_css,
            obj.id,
        )

    @button(change_form=True, html_attrs={"style": button_css})
    def Gravar(self, request):
        return redirect("/treinamento/gravar")
