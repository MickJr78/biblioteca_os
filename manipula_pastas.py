import os

name = ''


def cria_pasta(name):
    if not os.path.exists(f'{name}'):
        name = input('Digite o nome do novo diretório: ')
        os.mkdir(f'{name}')
        print(f'O DIRETORIO {name} FOI CRIADO COM SUCESSO!')
        

def excluir_pasta(name):
    name = input('Digite o nome do diretório a ser excluido: ')
    if not os.path.exists(name):
        print('O DIRETORIO {name} NAO EXISTE. TENTE NOVAMENTE.')
    elif os.path.exists(name):
        os.rmdir(f'{name}')
        print(f'O DIRETORIO {name} FOI EXCLUIDO COM SUCESSO!')


def decisao():
    try:
        opcao = input('Pressione C para Criar um diretório, e X para excluir um diretório: ')
        if opcao == 'C' or opcao == 'c':
            cria_pasta(name)
        elif opcao == 'X' or opcao == 'x':
            excluir_pasta(name)
        elif opcao != 'C' or opcao != 'X' or opcao != 'c' or opcao != 'x':
            print('OPCAO INVALIDA. TENTE NOVAMENTE')    
    except:
        if opcao == '':
            return 'VOCE PRECISA ESCOLHER UMA OPÇAO.'


# Chamar a função de decisão:
decisao()
