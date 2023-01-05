from django.contrib import admin
from NR10.models import *
from django.template.response import TemplateResponse
from admin_extra_buttons.api import ExtraButtonsMixin, button
from django.shortcuts import redirect
from django.urls import path
from django.db import models
from utils.css import *
from NR10.views import *


@admin.register(Nr10)
class Nr10Admin(admin.ModelAdmin):
    class Meta:
        model = Nr10


@admin.register(Nr10Complementar)
class Nr10ComplementarAdmin(admin.ModelAdmin):
    class Meta:
        model = Nr10Complementar


@admin.register(Aso)
class AsuAdmin(admin.ModelAdmin):
    class Meta:
        model = Aso


@admin.register(Autorizacao)
class AutorizacaoAdmin(admin.ModelAdmin):
    class Meta:
        model = Autorizacao


@admin.register(Roupa)
class RoupaAdmin(admin.ModelAdmin):
    class Meta:
        model = Roupa


@admin.register(Luva)
class LuvaAdmin(admin.ModelAdmin):
    class Meta:
        model = Luva


@admin.register(Capacete)
class CapaceteAdmin(admin.ModelAdmin):
    class Meta:
        model = Capacete


class Nr10ComplementarAdminInline(admin.TabularInline):
    model = Nr10Complementar
    verbose_name = "NR10 Complementar"
    verbose_name_plural = "NR10's Complementares"
    extra = 0


class Nr10AdminInline(admin.TabularInline):
    model = Nr10
    verbose_name = "NR10"
    verbose_name_plural = "NR10's"
    extra = 0


class AsuAdminInline(admin.TabularInline):
    model = Aso
    verbose_name = "Aso"
    verbose_name_plural = "Aso's"
    extra = 0


class AutorizacaoAdminInline(admin.StackedInline):
    model = Autorizacao
    verbose_name = "Autorização"
    verbose_name_plural = "Autorizações"
    extra = 0


class RoupaAdminInline(admin.TabularInline):
    model = Roupa
    extra = 0


class LuvaAdminInline(admin.StackedInline):
    model = Luva
    extra = 0


class CapaceteAdminInline(admin.StackedInline):
    model = Capacete
    extra = 0


@admin.register(Eletricista)
class EletricistaAdmin(ExtraButtonsMixin, admin.ModelAdmin):
    list_per_page = 15
    search_fields = ["nome", "id"]
    list_filter = [
        "cargo",
    ]
    list_display = [
        "nome",
        "expire_asu",
        "expire_Nr10",
        "expire_Nr10Complementar",
        "expire_Autorizacao",
        "expire_Luva",
        "expire_Capacete",
        "status_roupas",
    ]
    inlines = [
        Nr10AdminInline,
        Nr10ComplementarAdminInline,
        AsuAdminInline,
        AutorizacaoAdminInline,
        LuvaAdminInline,
        CapaceteAdminInline,
        RoupaAdminInline,
    ]

    @button(change_form=True, html_attrs={"style": button_css})
    def Importar(self, request):
        return redirect("/admin/NR10/extra")


class Extra(models.Model):
    ...


@admin.register(Extra)
class EletricistasPagesUteis(admin.ModelAdmin):
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path("", self.admin_site.admin_view(self.menu)),
            path("eletricista", self.admin_site.admin_view(subir_eletricista)),
            path("roupas", self.admin_site.admin_view(subir_roupas)),
            path("luvas", self.admin_site.admin_view(subir_luvas)),
            path("asu", self.admin_site.admin_view(subir_asu)),
        ]
        return my_urls + urls

    def menu(self, request):
        return TemplateResponse(request, "admin/NR10/menu.html")
