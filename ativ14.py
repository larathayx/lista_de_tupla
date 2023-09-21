#14. Crie uma tupla com números inteiros e crie uma nova tupla sem os elementos repetidos
tupla=(1, 1,2 ,3, 3, 4, 4, 5)
tupla_sem_repeticao=()

for elemento in tupla:
    if elemento not in tupla_sem_repeticao:
        tupla_sem_repeticao += (elemento,)

print(tupla_sem_repeticao)