#15. Crie uma tupla com nomes de frutas e encontre a posição de uma fruta específica
tupla_frutas=('banana', 'maçã', 'morango', 'uva', 'melancia') 
print(tupla_frutas)
fruta_procurada = input('Digite a posição da fruta que deseja localizar na tupla acima: ')
posicao= -1

for i in range(len(tupla_frutas)):
    if tupla_frutas[i] == fruta_procurada:
        posicao = i
        break

if posicao != -1:
    print(f"A fruta {fruta_procurada} está na posição {posicao} na tupla.")
else:
    print(f"A fruta {fruta_procurada} não foi encontrada na tupla.")