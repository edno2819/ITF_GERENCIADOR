from django.utils import timezone
from django.db import models
from django.utils.html import format_html
from djmoney.models.fields import MoneyField
from django.db import models
from django.contrib import admin
from gerenciador.settings import MEDIA_ROOT_ADMIN

class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return timezone.now()


class Equipamento(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=80, blank=False, null=False)
    descricao = models.CharField(default=" ", max_length=1024, blank=True)
    updated_at = AutoDateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.nome




class Manutenção(models.Model):
    STATUS = (
        ("Reparada", "Reparada"),
        ("Aguardando material", "Aguardando material"),
        ("Danificado", "Danificado"),
    )

    ESTOQUE = (
        ("Retornou para o campo", "Retornou para o campo"),
        ("Subconjunto New", "Subconjunto New"),
    )

    CURRENCY_CHOICES = (("USD", "Dolar"), ("BRL", "Real"))

    id = models.AutoField(primary_key=True)
    ordem = models.CharField(
        "Ordem de Serviço", max_length=15, blank=True, null=True
    )  # string 15
    area = models.ForeignKey(
        "utils.Area", on_delete=models.CASCADE, blank=True, null=True
    )
    equipamento = models.ForeignKey(
        "Equipamento",
        on_delete=models.CASCADE,
    )
    fabricante = models.CharField(max_length=40, blank=True, null=True)
    modelo = models.CharField(max_length=40, blank=True, null=True)
    n_serie = models.CharField(max_length=40, blank=True, null=True)
    recebimento = models.DateField(blank=True, null=True)
    anomalia = models.CharField(max_length=40, blank=True, null=True)
    custo_real = MoneyField(
        decimal_places=2,
        default=0,
        default_currency="BRL",
        currency_choices=CURRENCY_CHOICES,
        max_digits=11,
        blank=True,
        null=True,
    )
    material_disponivel = models.DateField(blank=True, null=True)  # data
    componentes_utilizados = models.CharField(max_length=40, blank=True, null=True)
    reparo = models.DateField(blank=True, null=True)  # data
    servico_executado = models.CharField(
        "Serviço executado", max_length=1024, blank=True, null=True
    )
    custo_reparo = MoneyField(
        decimal_places=2,
        default_currency="BRL",
        currency_choices=CURRENCY_CHOICES,
        max_digits=11,
        blank=True,
        null=True,
    )
    status = models.CharField(
        default="Danificado", max_length=30, choices=STATUS, blank=True, null=True
    )
    ganho = MoneyField(  # calcular automaticamente real vs economizado
        "Economizado",
        decimal_places=2,
        default_currency="BRL",
        currency_choices=CURRENCY_CHOICES,
        max_digits=11,
        blank=True,
        null=True,
    )
    estoque = models.CharField(
        max_length=50, blank=True, choices=ESTOQUE
    )  # opções retornou para o campo / subconjunto new

    estante = models.CharField(max_length=1, blank=True)  # numero de 1 a 6
    prateleria = models.CharField(max_length=1, blank=True)
    imagem = models.ImageField(
        "Foto do equipamento",
        upload_to=None,
        height_field=None,
        width_field=None,
        max_length=100,
        blank=True,
        null=True,
    )
    updated_at = AutoDateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return f"{self.equipamento}"

    class Meta:
        verbose_name_plural = "Manutenções"

    @admin.display()
    def showImg(self):
        path = str(self.imagem).replace('/', '\\')
        run = format_html(
            f'''<img
            style="width:60px; height: 50px;"
            src="{MEDIA_ROOT_ADMIN}\{path}"
            >''',
        )
        return run

