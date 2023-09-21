#3. Crie uma tupla com nomes de cores e ordene-a em ordem alfabética.

quant = int(input("Digite a quantidade de nomes você quer na lista: "))
tupla_nomes = ()
tupla_cores_ordenadas=()

for x in range(quant):
    nome = input("Digite o nome: ")
    tupla_nomes += (nome,)

# Conversao lista
lista_nomes = list(tupla_nomes)
lista_cores_ordenadas= list(tupla_cores_ordenadas)
while lista_nomes:
    menor_nome = lista_nomes[0]
    for nom in lista_nomes:
        if nom < menor_nome:
            menor_nome = nom
    lista_cores_ordenadas.append(menor_nome)
    lista_nomes.remove(menor_nome)

# Conversao tupla
nomes_ordenados = tuple(lista_cores_ordenadas)

print(nomes_ordenados)