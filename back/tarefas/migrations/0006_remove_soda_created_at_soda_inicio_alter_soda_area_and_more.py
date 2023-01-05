# Generated by Django 4.1.1 on 2022-11-11 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tarefas", "0005_remove_soda_prioridade"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="soda",
            name="created_at",
        ),
        migrations.AddField(
            model_name="soda",
            name="inicio",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="soda",
            name="area",
            field=models.CharField(
                choices=[
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
                ],
                default="-",
                max_length=40,
            ),
        ),
        migrations.AlterField(
            model_name="soda",
            name="comentario",
            field=models.CharField(default="", max_length=5048),
        ),
        migrations.AlterField(
            model_name="soda",
            name="descricao",
            field=models.CharField(default="", max_length=5048),
        ),
        migrations.AlterField(
            model_name="soda",
            name="responsavel",
            field=models.CharField(default="", max_length=60),
        ),
        migrations.AlterField(
            model_name="soda",
            name="situacao",
            field=models.CharField(
                choices=[
                    ("NOK", "Não Iniciado"),
                    ("AND", "Em Andamento"),
                    ("OK", "Finalizado"),
                ],
                default="NOK",
                max_length=3,
            ),
        ),
        migrations.AlterField(
            model_name="tarefa",
            name="comentario",
            field=models.CharField(default="", max_length=5048),
        ),
        migrations.AlterField(
            model_name="tarefa",
            name="descricao",
            field=models.CharField(default="", max_length=5048),
        ),
        migrations.DeleteModel(
            name="d",
        ),
    ]
