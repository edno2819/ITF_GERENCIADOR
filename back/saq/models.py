from django.utils import timezone
from django.db import models
from django.db import models

class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return timezone.now()


class DigitacaoProblema(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=80, blank=False, null=False)
    area = models.ForeignKey(
        "utils.Area", on_delete=models.CASCADE, blank=True, null=True
    )    
    item = models.CharField(max_length=80, blank=False, null=False)
    descricao = models.TextField(default=" ", max_length=1024, blank=True)
    create_at = AutoDateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.nome


class SugestaoMelhora(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=80, blank=False, null=False)
    id_ambev = models.CharField("ID Ambev", max_length=20, blank=True, null=True)
    area = models.ForeignKey(
        "utils.Area", on_delete=models.CASCADE, blank=True, null=True
    )    
    contribuicao = models.TextField("Contribuição", max_length=1024, blank=False, null=False)
    sugestao = models.TextField("Sugestão", max_length=1024, blank=False, null=False)
    create_at = AutoDateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = "Sugestões"
        verbose_name = "Sugestão"

class Apresentacao(models.Model):
    id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=80, blank=False, null=False)
    pdf = models.FileField(upload_to="saq/apresentacao/", max_length=254)
    edited_at = AutoDateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name_plural = "Apresentações"
        verbose_name = "Apresentação"
