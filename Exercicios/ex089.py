#Inicia varias listas e variaveis
alunos = []
nome = 0
media = 0

#Solicitaçao do numero de alunos
num_alunos = int(input('Quantos alunos deseja cadastrar? '))

#Loop para cadastrar alunos:
for i in range(num_alunos):
    nome = str(input(f'Nome aluno {i+1}: '))
    nota1 = float(input(f'Nota 1º: '))
    nota2 = float(input(f'Nota 2º: '))
    aluno = [nome,[nota1,nota2]]
    alunos.append(aluno[:])

#Impressao do Boletim dos Alunos
print('\nBoletim dos alunos:')
print('No. Nome          Média')
for i, aluno in enumerate(alunos):                 #Inicia o loop com 'for' que itera sobre a lista 'alunos' usando a funçao 'enumerate' que fornece o indice 'i' e o valor 'aluno'.
    media = sum(aluno[1])/2
    print(f'{i+1:<4}{aluno[0]:<16}{media:<6}')

#Consulta de notar individuais
while True:
    escolha = input('Deseja ver alguma nota individualmente? [S/N]: ').upper()[0]
    if escolha == 'N':
        break
    if escolha == 'S':
        al_es = int(input('Digite o número do aluno: '))
        if 1 <= al_es <= num_alunos:               #Verifica se o numero de alunos esta dentro do intervalo valido
            aluno = alunos[al_es - 1]              
            notas = aluno[1]
            print(f'Notas do aluno: {aluno[0]}: {notas[0]} e {notas[1]}')
        else:
            print('Número de aluno inválido.')
    else:
        print('Opção inválida.')

