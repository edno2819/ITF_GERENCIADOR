from django.db import models
from django.utils.html import format_html
from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html
from django.conf import settings


class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return timezone.now()


class Area(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=40, blank=False, null=False, unique=True)

    def __str__(self):
        return self.nome


class Arquivo(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=40, blank=False, null=False)
    path = models.CharField(max_length=300, blank=False, null=False)

    def __str__(self):
        return self.nome

    @admin.display(ordering="Ativar")
    def path_admin(self):
        return format_html(
            """
            <button style="border-radius: 8px; background-color:rgba(27, 189, 97, 0.258); padding: 6px;">
                {}
                </button>
        """,
            self.path,
        )


class Link(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=40, blank=False, null=False)
    link = models.CharField(max_length=300, blank=False, null=False)

    def __str__(self):
        return self.nome

    @admin.display(ordering="Ativar")
    def link_admin(self):
        return format_html(
            """
        <button style="
            border-radius: 13px;
            background-color: #4CAF50; /* Green */
            border: none;
            color: white;
            padding: 7px 32px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            "
        >
        <a style="text-decoration: none; color: white;" href="{}" target="_blank">Click aqui para abrir</a>
        </button>
        """,
            self.link,
        )


class Anotacao(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE, editable=False
    )
    nome = models.CharField(max_length=40, blank=False, null=False)
    anotacao = models.CharField(default=" ", max_length=10048)
    documento = models.FileField(
        upload_to="Utils/anotacao/", max_length=254, blank=True, null=True
    )
    updated_at = AutoDateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = "Anotações"

    def quote(self):
        if (
            self.anotacao[:80].find("<table") != -1
            or self.anotacao[:80].find("<img") != -1
        ):
            return format_html("Itens não mostraveis!")

        return format_html(f"<div>{self.anotacao[:80]}</div>")
