"""
amizades.py
-----------
Responsavel pelo gerenciamento de amizades entre usuarios.

Funcoes:
    - criar_amizade(usuarios): cria uma amizade entre dois usuarios
    - listar_amizades(usuarios): lista os amigos de um usuario
    - remover_amizade(usuarios): remove a amizade entre dois usuarios
"""

from usuarios import buscar_usuario_por_id


def criar_amizade(usuarios):

    print("\n--- CRIAR AMIZADE ---")

    # Le e valida o ID do primeiro usuario
    id1 = input("Digite o ID do primeiro usuario: ").strip()
    if not id1.isdigit():
        print("Erro: ID invalido! Digite apenas numeros inteiros.")
        return
    id1 = int(id1)

    # Le e valida o ID do segundo usuario
    id2 = input("Digite o ID do segundo usuario: ").strip()
    if not id2.isdigit():
        print("Erro: ID invalido! Digite apenas numeros inteiros.")
        return
    id2 = int(id2)

    # Impede que um usuario tente se adicionar como amigo de si mesmo
    if id1 == id2:
        print("Erro: um usuario nao pode ser amigo de si mesmo!")
        return

    # Verifica se ambos os usuarios existem
    usuario1 = buscar_usuario_por_id(usuarios, id1)
    usuario2 = buscar_usuario_por_id(usuarios, id2)

    if usuario1 is None:
        print(f"Erro: usuario com ID {id1} nao encontrado!")
        return

    if usuario2 is None:
        print(f"Erro: usuario com ID {id2} nao encontrado!")
        return

    # Verifica se a amizade ja existe para evitar duplicatas
    if id2 in usuario1["amigos"]:
        print(f"Atencao: {usuario1['nome']} e {usuario2['nome']} ja sao amigos!")
        return

    # Adiciona a amizade de forma bidirecional
    usuario1["amigos"].append(id2)
    usuario2["amigos"].append(id1)

    print(f"Sucesso: {usuario1['nome']} e {usuario2['nome']} agora sao amigos!")


def listar_amizades(usuarios):

    print("\n--- LISTAR AMIZADES ---")

    # Le e valida o ID do usuario
    id_usuario = input("Digite o ID do usuario: ").strip()
    if not id_usuario.isdigit():
        print("Erro: ID invalido! Digite apenas numeros inteiros.")
        return

    id_usuario = int(id_usuario)

    # Verifica se o usuario existe
    usuario = buscar_usuario_por_id(usuarios, id_usuario)
    if usuario is None:
        print(f"Erro: usuario com ID {id_usuario} nao encontrado!")
        return

    print(f"\nAmigos de {usuario['nome']}:")

    # Informa caso o usuario ainda nao tenha amigos
    if len(usuario["amigos"]) == 0:
        print("Este usuario ainda nao tem amigos.")
        return

    # Exibe os dados de cada amigo
    for id_amigo in usuario["amigos"]:
        amigo = buscar_usuario_por_id(usuarios, id_amigo)
        if amigo is not None:
            print(
                f"  -> ID: {amigo['id']} | "
                f"Nome: {amigo['nome']} | "
                f"Idade: {amigo['idade']}"
            )


def remover_amizade(usuarios):

    print("\n--- REMOVER AMIZADE ---")

    # Le e valida o ID do primeiro usuario
    id1 = input("Digite o ID do primeiro usuario: ").strip()
    if not id1.isdigit():
        print("Erro: ID invalido! Digite apenas numeros inteiros.")
        return
    id1 = int(id1)

    # Le e valida o ID do segundo usuario
    id2 = input("Digite o ID do segundo usuario: ").strip()
    if not id2.isdigit():
        print("Erro: ID invalido! Digite apenas numeros inteiros.")
        return
    id2 = int(id2)

    # Verifica se ambos os usuarios existem
    usuario1 = buscar_usuario_por_id(usuarios, id1)
    usuario2 = buscar_usuario_por_id(usuarios, id2)

    if usuario1 is None:
        print(f"Erro: usuario com ID {id1} nao encontrado!")
        return

    if usuario2 is None:
        print(f"Erro: usuario com ID {id2} nao encontrado!")
        return

    # Verifica se a amizade de fato existe antes de tentar remover
    if id2 not in usuario1["amigos"]:
        print(f"Atencao: {usuario1['nome']} e {usuario2['nome']} nao sao amigos!")
        return

    # Remove a amizade de forma bidirecional
    usuario1["amigos"].remove(id2)
    usuario2["amigos"].remove(id1)

    print(f"Amizade entre {usuario1['nome']} e {usuario2['nome']} removida com sucesso!")