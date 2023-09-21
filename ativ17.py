# 17. Crie uma tupla com nomes de países e suas respectivas populações, e encontre o país mais populoso.
quant = int(input("Digite a quantidade de paises que você quer na lista: "))
tupla_paises = ()
tupla_populacao=()

for x in range(quant):
    pais = (input("Digite o país: "))
    populacao=  int(input("Digite sua população em numeros: "))
    tupla_paises += (pais,)
    tupla_populacao += (populacao,)

pais_mais_populoso = ""
populacao_mais_populosa = 0

for i in range(len(tupla_paises)):
    if tupla_populacao[i] > populacao_mais_populosa:
        pais_mais_populoso = tupla_paises[i]
        populacao_mais_populosa = tupla_populacao[i]

print(f"O país mais populoso é {pais_mais_populoso} com uma população de {populacao_mais_populosa} pessoas.")
