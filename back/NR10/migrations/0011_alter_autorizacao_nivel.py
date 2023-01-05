# Generated by Django 4.1.3 on 2022-11-23 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("NR10", "0010_aso_rename_certificado_autorizacao_documento_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="autorizacao",
            name="nivel",
            field=models.CharField(
                choices=[
                    (
                        "Sistema desernegizado sob supervisão",
                        "Sistema desernegizado sob supervisão",
                    ),
                    ("Sistema desernegizado", "Sistema desernegizado"),
                    (
                        "Sistema energizado Baixa tensão",
                        "Sistema energizado Baixa tensão",
                    ),
                    (
                        "Sistema energizado Alta tensão",
                        "Sistema energizado Alta tensão",
                    ),
                ],
                default="Sistema desernegizado",
                max_length=254,
            ),
        ),
    ]