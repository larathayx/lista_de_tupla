#12. Crie uma tupla de datas (dia, mês, ano) e ordene-as da mais antiga para a mais recente.

quant = int(input("Digite a quantidade de datas que você quer na lista: "))
tupla_datas = ()


for x in range(quant):
    dia = input("Digite o dia (ex.: 30): ")
    mes = input("Digite o mes (ex.: 2): ")
    ano = input("Digite o ano (ex.: 2020): ")
    tupla_data1=(dia, mes, ano)
    tupla_datas += (tupla_data1,)

# Conversao lista
list_datas = list(tupla_datas)

for i in range(len(list_datas)):
    for j in range(i + 1, len(list_datas)):
        dia1, mes1, ano1 = list_datas[i]
        dia2, mes2, ano2 = list_datas[j]
        if (ano1, mes1, dia1) > (ano2, mes2, dia2):
            list_datas[i], list_datas[j] = list_datas[j], list_datas[i]

# Conversao tupla
datas_ordenadas = tuple(list_datas)

print(datas_ordenadas)
