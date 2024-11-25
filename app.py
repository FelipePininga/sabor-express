import os
import time
restaurantes=[{'nome':'Império do lanche','categoria':'hamburgueria','status':False},
              {'nome':'Salgados da Cris','categoria':'salgados','status':True},
              {'nome':'Açaí Palace','categoria':'açaí','status':False}]

def alterar_status():
    '''Esta função é responsável por alterar o estado do restaurante de ativo para inativo e vice versa'''
    exibir_subtitulo('Alternando Status do restaurante')
    nome_restaurante=input('Digite o nome do restaurante que será ATIVADO/DESATIVADO! ')
    restaurante_encontrado=False
    for restaurante in restaurantes:
        if nome_restaurante==restaurante['nome']:
            restaurante_encontrado=True
            restaurante['status']=not restaurante['status']
            mensagem=f'O restaurante {nome_restaurante} foi ativado com sucesso' if restaurante['status'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_encontrado:
        print('O restaurante não foi encontrado!')    
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    '''Esta função é responsáver por exibir o subtítulo de cada função chamada'''
    linha='*'*(len(texto))
    os.system('cls')
    print(linha)
    print(texto)
    print(linha)
    print()

def voltar_ao_menu_principal():
    '''Esta função é responsável por encerrar a função ativa e retornar para o menu principal'''
    input('\nDigite uma tecla para voltar ao menu principal: ')
    main()

def listar_restaurantes():
    '''Esta função é responsável por listar todos os restaurantes cadastrados'''
    exibir_subtitulo('Lista de restaurantes')
    print(f'{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | {'Status'}')
    for restaurante in restaurantes:
        nome_restaurante=restaurante['nome']
        categoria=restaurante['categoria']
        if restaurante['status']:
            ativo='ativo'
        else:
            ativo='inativo'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_ao_menu_principal()

def exibir_nome_do_programa():
    '''Esta função é responsável por exibir o nome do programa'''
    print('''
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░''')

def exibir_opcoes():
    '''Esta função é responsável por exibir as opções no menu principal'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar Estado do restaurante')
    print('4. Sair\n')

def opcao_invalida():
    '''Esta opção é responsável por exibir mensagem de erro de validação'''
    print('Opção inválida!\n')
    voltar_ao_menu_principal()

def finalizar_aplicativo():
   '''Esta função é responsável por encerrar o programa'''
   exibir_subtitulo('Finalizando o aplicativo')

def cadastrar_novo_restaurante():
    '''Esta função é responsável por cadastrar novos restaurantes na lista'''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante=input('Digite o nome do restaurante a ser cadastrado: ')
    categoria=input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante={'nome':nome_do_restaurante,'categoria':categoria,'status':False}
    if nome_do_restaurante in restaurantes:
        print(f'Já existe um restaurante cadastrado com esse nome!')
        time.sleep(2)
        cadastrar_novo_restaurante()
    else:    
        restaurantes.append(nome_do_restaurante)
        print(f'O restaurante {dados_do_restaurante} foi cadastrado com sucesso')
        voltar_ao_menu_principal()

def escolher_opcao():
    '''Esta função é responsável pela seleção das chamadas de funções no menu principal'''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida==1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida==2:
            listar_restaurantes()
        elif opcao_escolhida==3:
            alterar_status()
        elif opcao_escolhida==4:
            finalizar_aplicativo()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''Função principal'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__=='__main__':
    main()
