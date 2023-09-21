from ex115 import cadastro
from ex115 import limpeza
from ex115 import listagem

def menu():
    while True:
        print('=' * 40)
        print('MENU DE OPÇÕES:'.center(40))
        print('=' * 40)
        print('1 - Cadastrar nova pessoa')
        print('2 - Listar todas as pessoas cadastradas')
        print('3 - Limpar lista de pessoas')
        print('4 - Sair')
        print('=' * 40)
        opcao = int(input('Escolha uma opção: '))

        if opcao == 1:
            nome = input('Digite o nome: ')
            idade = input('Digite a idade: ')
            cadastro.cadastro(nome, idade)
            print('Pessoa cadastrada com sucesso!')
        elif opcao == 2:
            listagem.listar()
        elif opcao == 3:
            limpeza.limpar()
        elif opcao == 4:
            print('Encerrando programa.')
            break
        else:
            print('Opção inválida. Tente novamente.')

menu()

