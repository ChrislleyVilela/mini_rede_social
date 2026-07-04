import json
import os

ARQUIVO = "dados.json"


def salvar_dados(usuarios, proximo_id):
    # Monta o dicionario com todos os dados a serem salvos
    dados = {
        "proximo_id": proximo_id,
        "usuarios": usuarios
    }

    # Abre (ou cria) o arquivo e grava os dados em formato JSON
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)

    print("Dados salvos com sucesso!")


def carregar_dados():
    # Se o arquivo nao existir, inicia o sistema do zero
    if not os.path.exists(ARQUIVO):
        print("Nenhum dado salvo encontrado. Iniciando do zero.")
        return [], 1

    # Abre o arquivo existente e carrega os dados
    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)

    print(f"Dados carregados! {len(dados['usuarios'])} usuario(s) encontrado(s).")

    # Retorna a lista de usuarios e o proximo ID disponivel
    return dados["usuarios"], dados["proximo_id"]