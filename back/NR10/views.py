from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_exempt
from tablib import Dataset, Databook
from unidecode import unidecode
from tabula import read_pdf
from NR10.models import *


# ADMIN
@csrf_exempt
def subir_eletricista(request):
    # var
    cargo_index = 41
    nome_index = 11
    id_index = 0
    profissoes = [
        "TECNICO(A) EM ELETRICA I",
        "TECNICO(A) ELETROMECANICA III",
        "TECNICO(A) EM ELETRICA II",
        "TECNICO(A) ELETROMECANICA IV",
        "TECNICO.A INSTRU. AUTOMACAO I",
        "TECNICO.A INSTRU. AUTOMACAO II",
    ]

    if request.method == "POST":
        try:
            dataset = Dataset()
            file = request.FILES["file"]
            imported_data = dataset.load(file.read(), format="xlsx")
            for data in imported_data:
                if data[cargo_index] in profissoes:
                    b = Eletricista.objects.filter(id=data[id_index])
                    if len(b) == 0:
                        instan = Eletricista(
                            id=data[id_index],
                            nome=data[nome_index],
                            cargo=data[cargo_index],
                        )
                        instan.save()
        except:
            return TemplateResponse(
                request, "admin/NR10/subirEletricista.html", {"error": True}
            )

        return TemplateResponse(
            request, "admin/NR10/subirEletricista.html", {"result": True}
        )

    return TemplateResponse(request, "admin/NR10/subirEletricista.html")


@csrf_exempt
def subir_roupas(request):
    if request.method == "POST":
        try:
            dataset = Dataset()
            file = request.FILES["file"]
            imported_data = dataset.load(file.read(), format="xlsx")
            for data in imported_data:
                if data[cargo_index] in profissoes:
                    b = Eletricista.objects.filter(id=data[id_index])
                    if len(b) == 0:
                        instan = Eletricista(
                            id=data[id_index],
                            nome=data[nome_index],
                            cargo=data[cargo_index],
                        )
                        instan.save()
        except:
            return TemplateResponse(
                request, "admin/NR10/subirRoupas.html", {"error": True}
            )

        return TemplateResponse(
            request, "admin/NR10/subirRoupas.html", {"result": True}
        )

    return TemplateResponse(request, "admin/NR10/subirRoupas.html")


@csrf_exempt
def subir_luvas(request):
    if request.method == "POST":
        nomes_unfound = []

        file = request.FILES["file"]
        data = request.POST.get("data")
        pages = request.POST.get("pages").split(",")
        pages = [int(num) for num in pages]

        pdf = read_pdf(file, pages=pages)

        for dataframe in pdf:
            if len(dataframe.columns) == 6:
                df = dataframe.columns.to_frame().T.append(dataframe, ignore_index=True)
                df.columns = range(6)
                for _, row in df.iterrows():
                    if row[0].find("ELETRICISTA RESPONÁVEL: ") != -1:
                        nome = unidecode(row[0].split("ELETRICISTA RESPONÁVEL: ")[1])
                        elet = Eletricista.objects.filter(nome=nome)
                        if len(elet) == 1:
                            elet = elet[0]
                        else:
                            nomes_unfound.append(nome)
                    else:
                        status = True if row[5] == "APROVADA" else False
                        try:
                            luva_inst = Luva(
                                dono=elet,
                                status_exame=status,
                                ultimo_exame=data,
                                n_serie=str(row[3]),
                            )
                            luva_inst.save()
                        except Exception as e:
                            nomes_unfound.append(nome)
                            print("ERROR", e)

                print(nomes_unfound)
        nomes_unfound = list(set(nomes_unfound))
        return TemplateResponse(
            request,
            "admin/NR10/subirLuvas.html",
            {"result": True, "nao_achados": nomes_unfound},
        )

    return TemplateResponse(request, "admin/NR10/subirLuvas.html")


@csrf_exempt
def subir_asu(request):
    nomes_unfound = []

    # var
    id_index = 0
    data_exame = 5
    nome_exame = 1
    status_exame = 7
    sheet_name = "PERIODICO"

    if request.method == "POST":
        try:
            dataset = Databook()
            file = request.FILES["file"]
            imported_data = dataset.load(file.read(), format="xlsx")
            for data in imported_data.sheets():
                if data.title == sheet_name:
                    break

            for row in data:
                elet = Eletricista.objects.filter(id=row[id_index])

                if len(elet) == 1:
                    d = str(row[data_exame])
                    elet = elet[0]
                    aso_inst = Aso(
                        dono=elet,
                        status_exame=True if row[status_exame] == "OK" else False,
                        data=d[:10],
                    )
                    aso_inst.save()
                else:
                    nomes_unfound.append(row[nome_exame])

            print(nomes_unfound)

        except:
            return TemplateResponse(
                request, "admin/NR10/subirAsu.html", {"error": True}
            )

        return TemplateResponse(request, "admin/NR10/subirAsu.html", {"result": True})

    return TemplateResponse(request, "admin/NR10/subirAsu.html")
