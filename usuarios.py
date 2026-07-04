"""
usuarios.py
-----------
Responsável pelo gerenciamento de usuários da mini rede social.

Funções:
    - buscar_usuario_por_id(usuarios, id_buscado): busca e retorna um usuário pelo ID
    - cadastrar_usuario(usuarios, proximo_id): cadastra um novo usuário
    - listar_usuarios(usuarios): exibe todos os usuários cadastrados
    - remover_usuario(usuarios): remove um usuário e suas amizades
"""


def buscar_usuario_por_id(usuarios, id_buscado):

    for usuario in usuarios:
        if usuario["id"] == id_buscado:
            return usuario

    # Retorna None explicitamente se o usuário não for encontrado
    return None


def cadastrar_usuario(usuarios, proximo_id):

    print("\n--- CADASTRAR USUÁRIO ---")

    nome = input("Digite o nome do usuário: ").strip()
    if nome == "":
        print("Erro: nome não pode ser vazio!")
        return usuarios, proximo_id

    # Nome não pode ser composto apenas por números
    if nome.isdigit():
        print("Erro: nome não pode ser apenas números!")
        return usuarios, proximo_id

    # Lê e valida a idade do usuário
    idade = input("Digite a idade do usuário: ").strip()
    if not idade.isdigit():
        print("Erro: idade inválida! Digite apenas números inteiros.")
        return usuarios, proximo_id

    idade = int(idade)

    # Idade deve ser um valor realista entre 1 e 120
    if idade <= 0 or idade > 120:
        print("Erro: idade inválida! Digite uma idade entre 1 e 120.")
        return usuarios, proximo_id

    # Cria o dicionário do novo usuário
    novo_usuario = {
        "id": proximo_id,
        "nome": nome,
        "idade": idade,
        "amigos": []  # Lista de IDs dos amigos do usuário
    }

    usuarios.append(novo_usuario)

    print(f"Usuário '{nome}' cadastrado com sucesso! ID: {novo_usuario['id']}")

    # Retorna a lista atualizada e o próximo ID incrementado
    return usuarios, proximo_id + 1


def listar_usuarios(usuarios):

    print("\n--- LISTA DE USUÁRIOS ---")

    # Verifica se há usuários cadastrados antes de listar
    if len(usuarios) == 0:
        print("Nenhum usuário cadastrado ainda.")
        return

    for usuario in usuarios:
        quantidade_amigos = len(usuario["amigos"])
        print(
            f"ID: {usuario['id']} | "
            f"Nome: {usuario['nome']} | "
            f"Idade: {usuario['idade']} | "
            f"Amigos: {quantidade_amigos}"
        )


def remover_usuario(usuarios):

    print("\n--- REMOVER USUÁRIO ---")

    # Lê e valida o ID informado
    id_usuario = input("Digite o ID do usuário que deseja remover: ").strip()
    if not id_usuario.isdigit():
        print("Erro: ID inválido! Digite apenas números inteiros.")
        return usuarios

    id_usuario = int(id_usuario)

    # Verifica se o usuário existe
    usuario = buscar_usuario_por_id(usuarios, id_usuario)
    if usuario is None:
        print(f"Erro: usuário com ID {id_usuario} não encontrado!")
        return usuarios

    # Solicita confirmação antes de excluir
    confirmacao = input(
        f"Tem certeza que deseja remover '{usuario['nome']}'? (s/n): "
    ).strip().lower()

    if confirmacao != "s":
        print("Remoção cancelada.")
        return usuarios

    # Remove o ID deste usuário da lista de amigos de todos os outros
    for outro_usuario in usuarios:
        if id_usuario in outro_usuario["amigos"]:
            outro_usuario["amigos"].remove(id_usuario)

    nome_removido = usuario["nome"]
    usuarios.remove(usuario)

    print(f"Usuário '{nome_removido}' removido com sucesso!")

    return usuarios