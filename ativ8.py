# 8. Crie uma tupla com números inteiros e verifique se um número específico está presente.
tupla_num_int=(4, 5 , 10, 15, 5, 9, 3)

num_usuario = int(input("Digite o numero que voce deseja verificar se está na lista: "))

if num_usuario in (tupla_num_int):
    print("O numero está na lista")
else:
    print("O numero não está na lista")