from django.utils import timezone as tz
from django.utils.html import format_html
from django.db import models
from django.contrib import admin
import datetime


class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return tz.now()


def calculateDate(data, days_expiration):
    return (
        (data + datetime.timedelta(days=days_expiration)) - datetime.date.today()
    ).days


def htmlExpiracao(delta):
    if int(delta) > 0:
        return format_html(
            f"""<div
        style="background-color: #319c35; border:#319c35 ;color: rgb(255, 255, 255); border-radius: 5px;
        padding:5px"
        > Expira em {int(delta)} dias</div>"""
        )
    else:
        return format_html(
            f"""<div
        style="background-color: #a71c1c; border:#a71c1c ;color: rgb(255, 255, 255); border-radius: 5px;
        padding:5px"
        > Expirado à {int(delta) * -1} dias </div>"""
        )


def selectStyle(value):
    erro = "background-color: #a71c1c; border:#a71c1c ;color: rgb(255, 255, 255); border-radius: 5px; padding:2px; margin:3px"
    ok = "background-color: #319c35; border:#319c35 ;color: rgb(255, 255, 255); border-radius: 5px; padding:2px;margin:3px"
    return ok if value > 0 else erro


class Eletricista(models.Model):
    id = models.CharField(max_length=15, primary_key=True)
    nome = models.CharField(max_length=60, blank=False, null=False)
    area = models.ForeignKey(
        "utils.Area",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name="Área",
    )

    cargo = models.CharField(max_length=40, blank=True, null=True)
    imagem = models.ImageField(
        "Foto de Perfil",
        upload_to="NR10/foto/",
        height_field=None,
        width_field=None,
        max_length=100,
        blank=True,
        null=True,
    )

    def __str__(self):
        return f"{self.nome}"

    @admin.display(description="Aso")
    def expire_asu(self):
        last_asu = Aso.objects.filter(dono=self.id).latest("data")
        delta = calculateDate(last_asu.data, last_asu.expiracao)
        return htmlExpiracao(delta)

    @admin.display(description="Nr10")
    def expire_Nr10(self):
        last_Nr10 = Nr10.objects.filter(dono=self.id).latest("data")
        delta = calculateDate(last_Nr10.data, last_Nr10.expiracao)
        return htmlExpiracao(delta)

    @admin.display(description="Nr10Complementar")
    def expire_Nr10Complementar(self):
        last_Nr10Complementar = Nr10Complementar.objects.filter(dono=self.id).latest(
            "data"
        )
        delta = calculateDate(
            last_Nr10Complementar.data, last_Nr10Complementar.expiracao
        )
        return htmlExpiracao(delta)

    @admin.display(description="Luva")
    def expire_Luva(self):
        last_Luva = Luva.objects.filter(dono=self.id, status_exame=True).latest(
            "ultimo_exame"
        )
        delta = calculateDate(last_Luva.ultimo_exame, last_Luva.expiracao)
        return htmlExpiracao(delta)

    @admin.display(description="Capacete")
    def expire_Capacete(self):
        last_Capacete = Capacete.objects.filter(dono=self.id, status_exame=True).latest(
            "ultimo_exame"
        )
        delta = calculateDate(last_Capacete.ultimo_exame, last_Capacete.expiracao)
        return htmlExpiracao(delta)

    @admin.display(description="Roupa")
    def expire_Roupa(self):
        last_Roupa = Roupa.objects.filter(dono=self.id).latest("ultimo_exame")
        delta = calculateDate(last_Roupa.data, last_Roupa.expiracao)
        return htmlExpiracao(delta)

    def expire_Autorizacao(self):
        last_Autorizacao = Autorizacao.objects.filter(dono=self.id).latest("data")
        delta = calculateDate(last_Autorizacao.data, last_Autorizacao.expiracao)
        return htmlExpiracao(delta)

    @admin.display(description="Nivel Autorização")
    def autorizacao(self):
        last_auto = Autorizacao.objects.filter(dono=self.id).latest("data")
        return last_auto

    @admin.display(description="Status Roupas")
    def status_roupas(self):
        html = [
            "<div>",
        ]
        erro = "background-color: #a71c1c; border:#a71c1c ;color: rgb(255, 255, 255); border-radius: 5px; padding:5px"

        last_camisa = Roupa.objects.filter(dono=self.id, tipo="Camisa")
        last_calca = Roupa.objects.filter(dono=self.id, tipo="Calça")

        if last_camisa:
            last_camisa = last_camisa.latest("data")
            delta_camisa = calculateDate(last_camisa.data, last_camisa.expiracao)
            html.append(
                f"<li style='{selectStyle(delta_camisa)}'>Camisa: {delta_camisa} dias</li>"
            )
        # else:
        #     html.append(f"<li style='{selectStyle(0)}'>Camisa: Faltando</li>")

        if last_calca:
            last_calca = last_calca.latest("data")
            delta_calca = calculateDate(last_calca.data, last_calca.expiracao)
            html.append(
                f"<li style='{selectStyle(delta_calca)}'>Calça: {delta_calca} dias</li>"
            )
        # else:
        #     html.append(f"<li style='{selectStyle(0)}'>Calça: Faltando</li>")

        html.append("</div>")
        return format_html("".join(html))


class Nr10(models.Model):
    id = models.AutoField(primary_key=True)
    dono = models.ForeignKey(Eletricista, related_name="nr10", on_delete=models.CASCADE)
    data = models.DateField()
    certificado = models.FileField(upload_to="NR10/NR10/", max_length=254, blank=True, null=True)

    @property
    def expiracao(self):
        dias_expiracao = 365 * 2
        return dias_expiracao

    class Meta:
        verbose_name_plural = "NR10 Complementar"
        verbose_name = "NR10 Complementar"
        ordering = ["id"]

    def __str__(self):
        return f"NR10 de {self.dono}"


class Nr10Complementar(models.Model):
    id = models.AutoField(primary_key=True)
    dono = models.ForeignKey(
        Eletricista, related_name="nr10_Complementar", on_delete=models.CASCADE
    )
    data = models.DateField()
    certificado = models.FileField(upload_to="NR10/NR10Complementar/", max_length=254, blank=True, null=True)

    @property
    def expiracao(self):
        dias_expiracao = 365 * 2
        return dias_expiracao

    class Meta:
        verbose_name_plural = "NR10's Complementares"
        verbose_name = "NR10 Complementar"
        ordering = ["id"]

    def __str__(self):
        return f"NR10 de {self.dono}"


class Aso(models.Model):
    id = models.AutoField(primary_key=True)
    dono = models.ForeignKey(Eletricista, related_name="Aso", on_delete=models.CASCADE)
    data = models.DateField()
    status_exame = models.BooleanField("Status do Exame", editable=True)
    certificado = models.FileField(upload_to="NR10/ASO/", max_length=254, blank=True, null=True)

    @property
    def expiracao(self):
        dias_expiracao = 365
        return dias_expiracao

    class Meta:
        verbose_name = "ASO"
        verbose_name_plural = "ASO's"

    def __str__(self):
        return f"ASO de {self.dono}"


class Autorizacao(models.Model):
    NIVEL = (
        (
            "Sistema desernegizado sob supervisão",
            "Sistema desernegizado sob supervisão",
        ),
        ("Sistema desernegizado", "Sistema desernegizado"),
        ("Sistema energizado Baixa tensão", "Sistema energizado Baixa tensão"),
        ("Sistema energizado Alta tensão", "Sistema energizado Alta tensão"),
    )
    id = models.AutoField(primary_key=True)
    dono = models.ForeignKey(
        Eletricista, related_name="Autorização", on_delete=models.CASCADE
    )
    data = models.DateField()
    documento = models.FileField(upload_to="NR10/Autorizacao/", max_length=254)
    nivel = models.CharField(
        default="Sistema desernegizado", max_length=254, choices=NIVEL
    )

    @property
    def expiracao(self):
        dias_expiracao = 365
        return dias_expiracao

    @property
    def get_Days(self):
        return (self.data - tz.now()).days

    class Meta:
        verbose_name = "Autorização"
        verbose_name_plural = "Autorizações"

    def __str__(self):
        return self.nivel


class Luva(models.Model):
    LADO = (
        ("Esquerda", "Esquerda"),
        ("Direita", "Direita"),
    )
    STATUS = ((True, "OK"), (False, "Inrregular"))

    id = models.AutoField(primary_key=True)
    dono = models.ForeignKey(Eletricista, related_name="Luva", on_delete=models.CASCADE)
    n_serie = models.CharField("Nº de Série", max_length=20, blank=True, null=True)
    lado = models.CharField(default="Esquerda", max_length=20, choices=LADO)
    status_exame = models.BooleanField("Status do Exame", editable=True, choices=STATUS)
    ultimo_exame = models.DateField()

    @property
    def expiracao(self):
        dias_expiracao = 168
        return dias_expiracao

    def __str__(self):
        return str(self.dono)


class Capacete(models.Model):
    STATUS = ((True, "OK"), (False, "Inrregular"))

    id = models.AutoField(primary_key=True)
    dono = models.ForeignKey(
        Eletricista, related_name="Capacete", on_delete=models.CASCADE
    )
    n_serie = models.CharField("Nº de Série", max_length=20, blank=True, null=True)
    status_exame = models.BooleanField("Status do Exame", editable=True, choices=STATUS)
    ultimo_exame = models.DateField()

    @property
    def expiracao(self):
        dias_expiracao = 168
        return dias_expiracao

    def __str__(self):
        return str(self.dono)


class Roupa(models.Model):
    TIPO = (("Calça", "Calça"), ("Camisa", "Camisa"))

    id = models.AutoField(primary_key=True)
    dono = models.ForeignKey(
        Eletricista, related_name="Roupa", on_delete=models.CASCADE
    )
    n_serie = models.CharField("Nº de Série", max_length=20, blank=True, null=True)
    tipo = models.CharField(
        "Tipo de Roupa", max_length=20, default="Camisa", choices=TIPO
    )
    data = models.DateField()

    @property
    def expiracao(self):
        dias_expiracao = 365
        return dias_expiracao

    def __str__(self):
        return str(self.dono)
