#19. Crie uma tupla com números inteiros e verifique se todos os elementos são maiores que 10.
quant = int(input("Digite a quantidade de numeros que você quer na lista: "))
tupla_numeros = ()

for x in range(quant):
    num = (input("Digite o numero: "))
    tupla_numeros += (num,)

todos_maiores_dez = True

for numero in tupla_numeros:
    if numero <= 10:
        todos_maiores_que_10 = False
        break 

if todos_maiores_que_10:
    print("Todos os elementos da tupla são maiores que 10.")
else:
    print("Pelo menos um elemento da tupla não é maior que 10.")