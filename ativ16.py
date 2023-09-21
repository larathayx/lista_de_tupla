# 16. Crie duas tuplas de números e crie uma terceira tupla com a soma dos elementos correspondentes
tupla_um = (1, 2, 3, 4, 5)
tupla_dois = (3, 4, 5, 6, 7)
tupla_final = ()

for i in range(len(tupla_um)):
    soma = tupla_um[i] + tupla_dois[i]
    tupla_final += (soma,)

print(tupla_final)