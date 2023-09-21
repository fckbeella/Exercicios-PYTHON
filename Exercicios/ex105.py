def notas():
    alunos = int(input('Quantos alunos tem na sala: '))
    cont=0
    notas = []
    for c in range(alunos):
        notas.append(int(input('Digita a nota: ')))
        cont+=1
    tot = sum(notas)
    print(f'{cont} Notas foram contabilizadas.')
    print(f'{max(notas)} foi a maior nota.')
    print(f'{min(notas)} foi a menor nota.')
    print(f'{tot/cont} foi a media da turma.')


notas()