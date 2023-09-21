#9. Crie uma tupla com números inteiros e retorne uma nova tupla com os elementos pares.
quant = int(input("Digite a quantidade de numeros que você quer na lista: "))
tupla_num = ()
tupla_pares=()

for x in range(quant):
    num = int(input("Digite o numero: "))
    tupla_num += (num,)

# Conversao lista
list_num = list(tupla_num)
list_par = list(tupla_pares)

for n in list_num:
    if n % 2 == 0:
        list_par.append(n)
    
# Conversao tupla
tupla_pares = tuple(list_par)
print(tupla_pares)