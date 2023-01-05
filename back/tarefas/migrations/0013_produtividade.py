# Generated by Django 4.1.3 on 2022-12-02 13:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import tarefas.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("tarefas", "0012_tarefa_documento"),
    ]

    operations = [
        migrations.CreateModel(
            name="Produtividade",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("acao", models.CharField(max_length=40, verbose_name="Ação")),
                ("inicio", models.DateField(blank=True, null=True)),
                ("prazo", models.DateField(blank=True, null=True)),
                (
                    "status",
                    models.SmallIntegerField(
                        choices=[
                            (1, "Não Iniciado"),
                            (2, "Em Andamento"),
                            (3, "Finalizado"),
                        ],
                        default=1,
                    ),
                ),
                (
                    "descricao",
                    models.CharField(
                        blank=True, default="", max_length=5048, null=True
                    ),
                ),
                (
                    "comentario",
                    models.CharField(
                        blank=True, default="", max_length=5048, null=True
                    ),
                ),
                (
                    "documento",
                    models.FileField(
                        blank=True,
                        max_length=254,
                        null=True,
                        upload_to="Tarefas/tarefa/",
                    ),
                ),
                (
                    "created_at",
                    models.DateField(default=django.utils.timezone.now, editable=False),
                ),
                (
                    "updated_at",
                    tarefas.models.AutoDateTimeField(
                        default=django.utils.timezone.now, editable=False
                    ),
                ),
                (
                    "responsavel",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
