#5. Crie uma tupla com números inteiros e encontre o maior e o menor valor.
quant = int(input("Digite a quantidade de numeros que você quer na lista: "))
tupla_num = ()

for x in range(quant):
    num = int(input("Digite o numero: "))
    tupla_num += (num,)

# Conversao lista
list_num = list(tupla_num)

maior_numero = list_num[0]
menor_numero = list_num[0]

for numero in list_num:
    if numero > maior_numero:
        maior_numero = numero
    if numero < menor_numero:
        menor_numero = numero

print("O maior número na lista é:", maior_numero)
print("O menor número na lista é:", menor_numero)