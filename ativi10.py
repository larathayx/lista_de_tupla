#10. Crie uma tupla de palavras e crie uma nova tupla com o comprimento de cadapalavra.

quant = int(input("Digite a quantidade de palavras que você quer na lista: "))
tupla_paravras = ()
tupla_quant_letras=()

for x in range(quant):
    word = input("Digite a palavra: ")
    tupla_paravras += (word,)
    tamanho=len(word)
    tupla_quant_letras+=(tamanho,)

print("palavras: ", tupla_paravras)
print("quantidade de letras: ", tupla_quant_letras)
