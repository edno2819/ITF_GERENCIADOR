from django.core.exceptions import ValidationError
from django.conf import settings
from django.utils import timezone
from django.db import models
from django.utils.html import format_html


def validate_number(value):
    if type(value) != int or value > 10 or value < 0:
        raise ValidationError(
            "%s Value must be in range (0,10) and be a integer" % value
        )


class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return timezone.now()


class Tarefa(models.Model):
    NIVEIS_TAREFAS = (
        (1, "Baixo"),
        (2, "Medio Baixo"),
        (3, "Médio"),
        (4, "Alto"),
        (5, "Urgente"),
    )

    SITUACAO = (
        (1, "Não Iniciado"),
        (2, "Em Andamento"),
        (3, "Finalizado"),
    )

    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=40, blank=False, null=False)
    responsavel = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    prioridade = models.SmallIntegerField(choices=NIVEIS_TAREFAS)
    prazo = models.DateField(blank=True, null=True)
    situacao = models.SmallIntegerField(default=1, choices=SITUACAO)
    descricao = models.CharField(default="", max_length=5048, blank=True, null=True)
    comentario = models.CharField(default="", max_length=5048, blank=True, null=True)
    documento = models.FileField(
        upload_to="Tarefas/tarefa/", max_length=254, blank=True, null=True
    )
    created_at = models.DateField(default=timezone.now, editable=False)
    updated_at = AutoDateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.nome

    def status_tarefa(self):
        options = {1: "Não Iniciado", 2: "Em Andamento", 3: "Finalizado"}
        color = {1: "a71c1c", 2: "e5e619", 3: "319c35"}
        return format_html(
            """<button 
            style="background-color: #{}; border:#{} ;color: rgb(255, 255, 255); border-radius: 5px;"
            >{}</button>""",
            color[self.situacao],
            color[self.situacao],
            options[self.situacao],
        )

    def prioridade_tarefa(self):
        options = {1: "Baixo", 2: "Medio Baixo", 3: "Médio", 4: "Alto", 5: "Urgente"}
        color = {1: "00ff00", 2: "0000ff", 3: "319c35", 4: "ffea00", 5: "a71c1c"}
        return format_html(
            """<button 
            style="background-color: #{}; border:#{} ;color: rgb(255, 255, 255); border-radius: 5px;"
            >{}</button>""",
            color[self.prioridade],
            color[self.prioridade],
            options[self.prioridade],
        )


class Projeto(models.Model):
    NIVEIS_PROJETOS = (
        (1, "Baixo"),
        (2, "Medio Baixo"),
        (3, "Médio"),
        (4, "Alto"),
        (5, "Urgente"),
    )

    SITUACAO = (
        (1, "Não Iniciado"),
        (2, "Em Andamento"),
        (3, "Finalizado"),
    )

    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=40, blank=False, null=False)
    responsavel = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    prioridade = models.SmallIntegerField(choices=NIVEIS_PROJETOS)
    inicio = models.DateField(blank=True, null=True)
    prazo = models.DateField(blank=True, null=True)
    situacao = models.SmallIntegerField(default=1, choices=SITUACAO)
    descricao = models.CharField(max_length=5048, blank=True, null=True)
    comentario = models.CharField(max_length=5048, blank=True, null=True)

    def __str__(self):
        return self.nome

    @property
    def username(self):
        return self.responsavel.first_name

    def status_tarefa(self):
        options = {1: "Não Iniciado", 2: "Em Andamento", 3: "Finalizado"}
        color = {1: "a71c1c", 2: "e5e619", 3: "319c35"}
        return format_html(
            """<button 
            style="background-color: #{}; border:#{} ;color: rgb(255, 255, 255); border-radius: 5px;"
            >{}</button>""",
            color[self.situacao],
            color[self.situacao],
            options[self.situacao],
        )

    def prioridade_tarefa(self):
        options = {1: "Baixo", 2: "Medio Baixo", 3: "Médio", 4: "Alto", 5: "Urgente"}
        color = {1: "00ff00", 2: "0000ff", 3: "319c35", 4: "ffea00", 5: "a71c1c"}
        return format_html(
            """<button 
            style="background-color: #{}; border:#{} ;color: rgb(255, 255, 255); border-radius: 5px;"
            >{}</button>""",
            color[self.prioridade],
            color[self.prioridade],
            options[self.prioridade],
        )


class Soda(models.Model):
    AREAS = (
        ("-", "-"),
        ("Brassagem 01", "Brassagem 1"),
        ("Brassagem 02", "Brassagem 2"),
        ("Filtração 1", "Filtração 1"),
        ("Filtração 2", "Filtração 2"),
        ("L502", "L502"),
        ("L503", "L503"),
        ("L511", "L511"),
        ("L512", "L512"),
        ("Maturação", "Maturação"),
        ("Qualidade", "Qualidade"),
        ("Utilidades", "Utilidades"),
        ("Maturação", "Maturação"),
        ("Adega de Fermento", "Adega de Fermento"),
    )

    SITUACAO = (
        ("NOK", "Não Iniciado"),
        ("AND", "Em Andamento"),
        ("OK", "Finalizado"),
    )

    id = models.AutoField(primary_key=True)
    area = models.CharField(max_length=40, default="-", choices=AREAS)
    nome = models.CharField(max_length=40, blank=False, null=False)
    inicio = models.DateField(blank=True, null=True)
    prazo = models.DateField(blank=True, null=True)
    responsavel = models.CharField(default="", max_length=60, blank=False, null=False)
    status = models.CharField(default="NOK", max_length=3, choices=SITUACAO)
    comentario = models.CharField(default=" ", max_length=70, blank=True)
    descricao = models.CharField(default=" ", max_length=5048, blank=True)
    updated_at = AutoDateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "SODA"

    def status_tarefa(self):
        options = {"NOK": "Não Iniciado", "AND": "Em Andamento", "OK": "Finalizado"}
        color = {"NOK": "a71c1c", "AND": "e5e619", "OK": "319c35"}
        return format_html(
            """<button 
            style="background-color: #{}; border:#{} ;color: rgb(255, 255, 255); border-radius: 5px;"
            >{}</button>""",
            color[self.status],
            color[self.status],
            options[self.status],
        )

    def prioridade_tarefa(self):
        options = {1: "Baixo", 2: "Medio Baixo", 3: "Médio", 4: "Alto", 5: "Urgente"}
        color = {1: "00ff00", 2: "0000ff", 3: "319c35", 4: "ffea00", 5: "a71c1c"}
        return format_html(
            """<button 
            style="background-color: #{}; border:#{} ;color: rgb(255, 255, 255); border-radius: 5px;"
            >{}</button>""",
            color[self.prioridade],
            color[self.prioridade],
            options[self.prioridade],
        )

    def observacoes(self):
        return format_html(self.comentario)


class Produtividade(models.Model):
    SITUACAO = (
        (1, "Não Iniciado"),
        (2, "Em Andamento"),
        (3, "Finalizado"),
    )

    id = models.AutoField(primary_key=True)
    acao = models.CharField("Ação", max_length=80, blank=False, null=False)
    responsavel = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    inicio = models.DateField(blank=True, null=True)
    prazo = models.DateField(blank=True, null=True)
    status = models.SmallIntegerField(default=1, choices=SITUACAO)
    descricao = models.CharField(default="", max_length=5048, blank=True, null=True)
    comentario = models.CharField(default=" ", max_length=70, blank=True)
    documento = models.FileField(
        upload_to="Tarefas/tarefa/", max_length=254, blank=True, null=True
    )
    created_at = models.DateField(default=timezone.now, editable=False)
    updated_at = AutoDateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.acao