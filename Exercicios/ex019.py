import random
a = input('Escreva o nome dos alunos separados por vírgula: ').split(", ")
print(f'O escolhido foi: {random.choice(a)}')