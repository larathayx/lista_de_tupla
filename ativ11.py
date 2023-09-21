#11. Crie uma tupla com números inteiros e calcule a média dos valores.
quant = int(input("Digite a quantidade de numeros que você quer na lista: "))
tupla_numeros = ()

for x in range(quant):
    num = input("Digite o numero: ")
    tupla_numeros += (num,)

# Conversao lista
list_numeros = list(tupla_numeros)

soma=sum(list_numeros)
media=soma/quant
print("media: ", str(media))
