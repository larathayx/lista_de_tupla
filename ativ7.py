#7. Crie uma tupla de strings e conte quantas delas têm mais de 5 caracteres
quant = int(input("Digite a quantidade de palavras que você quer na lista: "))
tupla_words = ()
tupla_long_words = ()

for x in range(quant):
    word = (input("Digite a palavra: "))
    tupla_words += (word,)

# Conversao lista
list_words = list(tupla_words)
list_long_words = list(tupla_long_words)

for word in list_words:
    if len(word) > 5:
        list_long_words.append(word)

tamanho=len(list_long_words)

# Conversao tupla
tupla_cinco_elem= tuple(list_long_words)

print("Quantidade de palavras com mais de 5 letras:", str(tamanho))
print(" Palavras com mais de 5 letras: ", tupla_cinco_elem)