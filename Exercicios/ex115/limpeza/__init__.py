#A função Limpar  tem o objetivo de apagar todos os registros contidos no arquivo "pessoas.txt".
# - with open('pessoas.txt', 'w') as arquivo:: Aqui, estamos abrindo o arquivo "pessoas.txt" em
# modo de escrita ('w'). Isso significa que estamos abrindo o arquivo para escrita e, caso ele não
# exista, um novo arquivo será criado. O uso do gerenciador de contexto with garante que o arquivo
# será automaticamente fechado após o uso, evitando vazamentos de recursos.
# - arquivo.truncate(0): Esta linha é responsável por "truncar" o arquivo, ou seja, apagar todos
# os dados que estão atualmente no arquivo. O argumento 0 passado para o método truncate indica que
# queremos apagar tudo, desde o início do arquivo até o final.


def limpar():
    try:
        with open('pessoas.txt', 'w') as arquivo:                        #w = escrita e o truncate = esvaziado
            arquivo.truncate(0)
        print('Lista de pessoas foi apagada com sucesso.')
    except FileNotFoundError:
        print('Nenhuma pessoa cadastrada.')
