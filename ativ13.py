# 13. Crie uma tupla com números inteiros e verifique se todos os elementos são pares.

quant = int(input("Digite a quantidade de numeros que você quer na lista de verificação: "))
tupla_numeros = ()

for x in range(quant):
    num = int(input("Digite o numero: "))
    tupla_numeros += (num,)

# Conversao lista
list_numeros = list(tupla_numeros)
list_pares=[]

for num in list_numeros:
    if num % 2 == 0:
        list_pares.append(num)

if list_pares == list_numeros:
    print("são todos iguais")
else:
    print("não são todos iguais")
    

