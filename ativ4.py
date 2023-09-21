#4. Crie uma tupla com números inteiros e retorne a soma de todos os elementos.

quant = int(input("Digite a quantidade de numeros que você quer na lista: "))
tupla_num = ()

for x in range(quant):
    num = int(input("Digite o numero: "))
    tupla_num += (num,)

# Conversao lista
lista_num = list(tupla_num)
soma= sum(lista_num)

print("soma: ", str(soma))