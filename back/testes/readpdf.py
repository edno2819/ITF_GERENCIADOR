from tabula import read_pdf
from unidecode import unidecode

#remover acentos
pdf = read_pdf(r'C:\Users\ITF-04\Desktop\edno\Gerenciador-de-tarefas\TEMP\Ensaios-Luvas-Ambev-ma-ago-2022-D4Sign.pdf', pages=[6,7,8,9,10])

for dataframe in pdf:
    if len(dataframe.columns)==6:
        df = dataframe.columns.to_frame().T.append(dataframe, ignore_index=True)
        df.columns = range(6)
        for _, row in df.iterrows():
            if row[0].find('ELETRICISTA RESPONÁVEL: ')!=-1:
                nome = unidecode(row[0].split('ELETRICISTA RESPONÁVEL: ')[1])
                id = 'Eletricista.objects.find(nome=nome).id'
            else:
                status = True if row[5]=="APROVADA" else False
                print(row)
