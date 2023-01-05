from django.db import models
from django.utils.html import format_html
from django.core.validators import FileExtensionValidator
from django.utils import timezone


class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return timezone.now()


class Referencia(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=40, blank=False, null=False)
    descricao = models.CharField(default=' ', max_length=1200, blank=True, null=True)
    link = models.CharField(max_length=300, blank=False, null=False)

    def link_aula(self):
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

    def descricao_aula(self):
        return format_html(self.descricao)


class Aula(models.Model):
    list_per_page = 30
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=70, blank=False, null=False)
    descricao = models.CharField(max_length=1200, blank=True, null=True)
    video = models.FileField(
        upload_to="videos_uploaded",
        null=True,
        validators=[
            FileExtensionValidator(
                allowed_extensions=["MOV", "avi", "mp4", "webm", "mkv"]
            )
        ],
    )
    create_at = AutoDateTimeField(default=timezone.now, editable=False)

