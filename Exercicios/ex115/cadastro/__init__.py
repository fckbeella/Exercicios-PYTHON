#Esta função é responsável por cadastrar uma pessoa no arquivo "pessoas.txt".
# -with open('pessoas.txt', 'a') as arquivo:: Abre o arquivo "pessoas.txt" no modo de escrita ('a').
# O modo 'a' significa "append", que permite adicionar novos dados ao final do arquivo sem apagar
# o conteúdo existente.
# -arquivo.write(f'{nome},{idade}\n'): Escreve os dados da pessoa (nome e idade) no arquivo no
# formato "nome,idade", seguido de uma quebra de linha (\n) para separar os registros.
# Isso permite que você adicione novas pessoas ao arquivo.

def cadastro(nome, idade):
    with open('pessoas.txt', 'a') as arquivo:       #a = append (acrescentar ao final do arquivo)
        arquivo.write(f'{nome}, {idade}\n')
