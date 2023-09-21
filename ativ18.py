# 18. Crie uma tupla com notas de alunos e retorne uma nova tupla com as notas em ordem crescente.
quant = int(input("Digite a quantidade de alunos que você quer na lista: "))
tupla_alunos = ()
tupla_notas=()

for x in range(quant):
    aluno = (input("Digite o nome do aluno: "))
    nota=  float(input("Digite sua nota: "))
    tupla_alunos += (aluno,)
    tupla_notas += (nota,)

tamanho = len(tupla_notas)
notas_ordenadas = list(tupla_notas)

for i in range(tamanho):
    for j in range(0, tamanho - i - 1):
        if notas_ordenadas[j] > notas_ordenadas[j + 1]:
            notas_ordenadas[j], notas_ordenadas[j + 1] = notas_ordenadas[j + 1], notas_ordenadas[j]

tupla_notas_ordenadas = tuple(notas_ordenadas)

print("Notas em ordem crescente:", tupla_notas_ordenadas)
