"""
main.py
-------
Ponto de entrada da Mini Rede Social.
Exibe o menu principal e delega as ações aos módulos responsáveis.

Módulos utilizados:
    - dados.py    : armazenamento dos dados em JSON
    - usuarios.py : cadastro, listagem e remoção de usuários
    - amizades.py : criação, listagem e remoção de amizades
"""
from dados import salvar_dados, carregar_dados
from usuarios import cadastrar_usuario, listar_usuarios, remover_usuario
from amizades import criar_amizade, listar_amizades, remover_amizade


def exibir_menu():
        
        print("  +==============================+  ")
        print("  |       MINI REDE SOCIAL       |  ")
        print("  +==============================+  ")
        print("  |  1. Cadastrar usuario        |  ")
        print("  |  2. Listar usuarios          |  ")
        print("  |  3. Criar amizade            |  ")
        print("  |  4. Listar amizades          |  ")
        print("  |  5. Remover amizade          |  ")
        print("  |  6. Remover usuario          |  ")
        print("  |  0. Sair                     |  ")
        print("  +==============================+  ")


def menu():

    usuarios, proximo_id = carregar_dados()
    while True:

        exibir_menu() 
        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            usuarios, proximo_id = cadastrar_usuario(
                usuarios,
                proximo_id
            )

        elif opcao == "2":
            listar_usuarios(usuarios)

        elif opcao == "3":
            criar_amizade(usuarios)

        elif opcao == "4":
            listar_amizades(usuarios)

        elif opcao == "5":
            remover_amizade(usuarios)

        elif opcao == "6":
            usuarios = remover_usuario(usuarios)

        elif opcao == "0":

            salvar_dados(usuarios, proximo_id)

            print("\nEncerrando o sistema. Até logo!")
            break

        else:
            print("Opção inválida! Digite um número do menu.")

# Ponto de entrada: executa o menu apenas se este for o arquivo principal
if __name__ == "__main__":
    menu()