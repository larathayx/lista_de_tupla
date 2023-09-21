quant = int(input("Digite a quantidade de animais que você quer na lista: "))
tupla_animais = ()

for x in range(quant):
    animal = input("Digite o nome do animal: ")  # Corrigido de "aninal" para "animal"
    tupla_animais += (animal,)

lista_animais = list(tupla_animais)

lista_animais.sort()

primeiros_tres_animais = lista_animais[:3]

print("Os três primeiros animais em ordem alfabética são:", primeiros_tres_animais)
