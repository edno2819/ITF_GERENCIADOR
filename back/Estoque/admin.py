from django.contrib import admin
from Estoque.models import *
from django_summernote.admin import SummernoteModelAdmin
from import_export.admin import ImportExportActionModelAdmin


@admin.register(Equipamento)
class EquipamentoAdmin(admin.ModelAdmin):
    list_per_page = 30
    list_display = ["nome", "descricao", "updated_at"]

    class Meta:
        model = Equipamento


@admin.register(Manutenção)
class ManutençãoAdmin(SummernoteModelAdmin, ImportExportActionModelAdmin):
    list_per_page = 30
    summernote_fields = "servico_executado"
    search_fields = ["equipamento", "ordem"]
    list_display = ["equipamento", "ordem", "area", "recebimento", "reparo", "status", "showImg"]
    # readonly_fields = [..., "headshot_image"]

    # def headshot_image(self, obj):
    #     return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
    #         url = obj.headshot.url,
    #         width=obj.headshot.width,
    #         height=obj.headshot.height,
    #         )
    # )