from django.contrib import admin
from tarefas.models import *
from django_summernote.admin import SummernoteModelAdmin
from django.db.models import Count
from django.db import connection
from django.contrib.auth.models import User
from import_export.admin import ImportExportActionModelAdmin
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter


@admin.register(Tarefa)
class tarefaAdmin(SummernoteModelAdmin):
    list_per_page = 30
    summernote_fields = ("descricao", "comentario")
    search_fields = ["nome"]
    list_filter = ["responsavel", "prioridade", "situacao", "prazo"]
    list_display = [
        "nome",
        "responsavel",
        "prazo",
        "prioridade_tarefa",
        "status_tarefa",
    ]
    change_list_template = "tarefas.html"

    def pizza_query(self):
        SITUACAO = {1: "Não Iniciado", 2: "Em Andamento", 3: "Finalizado"}

        with connection.cursor() as c:
            c.execute(
                "SELECT situacao, COUNT(*) FROM tarefas_Tarefa GROUP BY situacao;"
            )
            row = [list(row) for row in c.fetchall()]
            row = [[SITUACAO[cod], value] for cod, value in row]
            return row

    def changelist_view(self, request, extra_context=None):
        data = [["Nome", "Não Iniciadas", "Em Andamento", "Feitas"]]
        responsaveis = [
            res["responsavel"]
            for res in Tarefa.objects.all().values("responsavel").distinct()
        ]
        for res in responsaveis:
            new_col = [User.objects.get(pk=res).username]
            for situacao in [1, 2, 3]:
                Tarefa.objects.annotate(peoples=Count("situacao"))
                new_col.append(
                    Tarefa.objects.filter(responsavel=res, situacao=situacao).aggregate(
                        Count("situacao")
                    )["situacao__count"]
                )
            data.append(new_col)

        pizza_data = [["Situação", "Quantidade"]] + self.pizza_query()
        extra_context = {"bar_data": data, "pizza_data": pizza_data}
        return super().changelist_view(request, extra_context=extra_context)


@admin.register(Soda)
class SodaAdmin(SummernoteModelAdmin, ImportExportActionModelAdmin):
    list_per_page = 30
    summernote_fields = "descricao"
    list_editable = ["status", "comentario", "responsavel"]
    search_fields = ["nome"]
    list_filter = [
        "area",
        "responsavel",
        "status",
        "inicio",#("inicio", DateRangeFilter),
        "prazo",#("prazo", DateRangeFilter),
    ]
    list_display = [
        "area",
        "nome",
        "responsavel",
        "inicio",
        "prazo",
        "status",
        "comentario",
    ]

    class Meta:
        model = Soda
        import_id_fields = (
            "area",
            "nome",
            "responsavel",
            "prazo",
        )


@admin.register(Projeto)
class projetosAdmin(SummernoteModelAdmin):
    list_per_page = 30
    summernote_fields = ("descricao", "comentario")
    search_fields = ["nome"]
    list_filter = ["responsavel", "prioridade", "situacao", "prazo"]
    list_display = [
        "nome",
        "responsavel",
        "inicio",
        "prazo",
        "prioridade_tarefa",
        "status_tarefa",
    ]
    change_list_template = "projetos_admin.html"


@admin.register(Produtividade)
class ProdutividadeAdmin(SummernoteModelAdmin, ImportExportActionModelAdmin):
    list_per_page = 30
    summernote_fields = ["descricao"]
    list_editable = ["status", "prazo", "comentario"]
    search_fields = ["acao", ]
    list_filter = [
        "responsavel",
        "status",
        "inicio",#("inicio", DateRangeFilter),
        "prazo",#("prazo", DateRangeFilter),
    ]
    list_display = [
        "acao",
        "responsavel",
        "inicio",
        "prazo",
        "status",
        "comentario",
    ]

    class Meta:
        model = Produtividade

