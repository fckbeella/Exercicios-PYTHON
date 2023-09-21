#A função Listar  é responsável por listar todas as pessoas cadastradas no arquivo "pessoas.txt".
# - with open('pessoas.txt', 'r') as arquivo:: Abre o arquivo "pessoas.txt" no modo de leitura ('r').
# Isso permite que o programa leia os dados do arquivo.
# - pessoas = arquivo.readlines(): Lê todas as linhas do arquivo e armazena-as em uma lista chamada
# pessoas. Cada linha contém o nome e a idade de uma pessoa no formato "nome,idade".
# - nome, idade = pessoa.strip().split(','): Divide cada linha (representando uma pessoa) em duas
# partes, nome e idade, usando a vírgula como delimitador. A função strip() é usada para remover
# espaços em branco e quebras de linha extras.

def listar():
    try:
        with open('pessoas.txt', 'r') as arquivo:   #r = leitura
            pessoas = arquivo.readlines()
            if not pessoas:
                print('Nenhuma pessoa cadastrada.')
            else:
                print('Pessoas cadastradas:')
                for pessoa in pessoas:
                    nome, idade = pessoa.strip().split(',',1)                   #1 para dividir apenas a primeira vírgula encontrada em cada linha. Dessa forma, você garantirá que o nome completo seja atribuído à variável "nome" e o restante da linha, incluindo possíveis vírgulas na idade
                    print(f'Nome: {nome:<24} {idade} anos')
    except FileNotFoundError:
        print('Nenhuma pessoa cadastrada.')