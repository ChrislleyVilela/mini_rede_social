# Mini Rede Social

Trabalho Final - Disciplina: Algoritmo, Estruturas de Dados e Programacao
Professor: Joselito Junior - PiauÃ­Â­ Instituto de Tecnologia (PIT)

---

## Descricao

Sistema que simula as funcionalidades basicas de uma rede social,
desenvolvido em Python estruturado com funcoes, listas, dicionarios e JSON.
O projeto e organizado em modulos separados por responsabilidade.

---

## Funcionalidades

- Cadastrar usuarios (nome, idade, ID automatico)
- Listar todos os usuarios cadastrados
- Criar amizade entre dois usuarios (bidirecional)
- Listar amizades de um usuario
- Remover amizade entre dois usuarios
- Remover usuario (remove todas as amizades junto)
- Salvar e carregar dados automaticamente (JSON)

---

## Estrutura do Projeto

```
mini_rede_social/
|
+-- main.py       -> menu principal e inicio do programa
+-- usuarios.py   -> cadastrar, listar e remover usuarios
+-- amizades.py   -> criar, listar e remover amizades
+-- dados.py      -> salvar e carregar dados em JSON
+-- dados.json    -> criado automaticamente ao salvar
+-- README.md     -> documentacao do projeto
```

---

# COMO EXECUTAR O PROGRAMA - PASSO A PASSO

## PASSO 1 - Verificar se o Python esta instalado

Abra o Prompt de Comando do Windows:
  1. Pressione as teclas WINDOWS + R ao mesmo tempo
  2. Digite:  cmd
  3. Pressione Enter

Uma janela preta vai abrir. Dentro dela, digite:

    python --version

O que pode aparecer:

  a) Python 3.x.x  ->  esta instalado, pode ir para o PASSO 3
  b) Mensagem de erro  ->  precisa instalar, va para o PASSO 2

---

## PASSO 2 - Instalar o Python (so se precisar)

  1. Abra o navegador e acesse:  https://python.org/downloads
  2. Clique no botao amarelo  "Download Python 3.x.x"
  3. Abra o arquivo baixado
  4. IMPORTANTE: antes de clicar em instalar, marque a caixa:

        [X] Add Python to PATH

     (essa opcao fica na parte de baixo da tela de instalacao)

  5. Clique em  "Install Now"
  6. Aguarde a instalacao terminar
  7. Feche e abra o Prompt de Comando novamente
  8. Digite  python --version  para confirmar que foi instalado

---

## PASSO 3 - Baixar os arquivos do projeto

Baixe os seguintes arquivos:

    main.py
    usuarios.py
    amizades.py
    dados.py
    README.md

---

## PASSO 4 - Criar a pasta do projeto

  1. Va ate a Area de Trabalho (Desktop)
  2. Clique com o botao direito do mouse
  3. Clique em  "Nova pasta"
  4. Nomeie a pasta como:  mini_rede_social
  5. Abra a pasta
  6. Cole os 5 arquivos baixados dentro dela

A pasta deve ficar assim:

    mini_rede_social/
    +-- main.py
    +-- usuarios.py
    +-- amizades.py
    +-- dados.py
    +-- README.md

ATENCAO: todos os arquivos devem estar na mesma pasta.
Se algum arquivo estiver fora, o programa nao vai funcionar.

---

## PASSO 5 - Abrir o terminal dentro da pasta correta

Este e o passo mais importante.
O terminal precisa estar aberto DENTRO da pasta do projeto.

Jeito mais facil (recomendado):
  1. Abra a pasta  mini_rede_social  no Explorer do Windows
  2. Clique na barra de endereco no topo da janela
     (onde aparece o caminho como  C:\Users\SeuNome\Desktop\mini_rede_social)
  3. Apague o que esta escrito e digite:  cmd
  4. Pressione Enter

O terminal ja vai abrir direto dentro da pasta certa.

Para confirmar que esta na pasta certa, digite:

    dir

Deve aparecer os arquivos do projeto listados:

    main.py
    usuarios.py
    amizades.py
    dados.py
    README.md

Se apareceram esses arquivos, esta tudo certo. Pode ir para o PASSO 6.

---

## PASSO 6 - Executar o programa

Com o terminal aberto dentro da pasta, digite:

    python main.py

Pressione Enter.

O programa vai iniciar e mostrar o menu:

    Nenhum dado salvo encontrado. Iniciando do zero.

    +==============================+
    |       MINI REDE SOCIAL       |
    +==============================+
    |  1. Cadastrar usuario        |
    |  2. Listar usuarios          |
    |  3. Criar amizade            |
    |  4. Listar amizades          |
    |  5. Remover amizade          |
    |  6. Remover usuario          |
    |  0. Sair                     |
    +==============================+

    Escolha uma opcao:

O programa esta funcionando.

---

## PASSO 7 - Usar o programa

O programa funciona pelo teclado. Digite o numero da opcao e pressione Enter.

Exemplo de uso completo:

  Digite 1  ->  para cadastrar um usuario
               Sera pedido o nome e a idade
               Exemplo: nome = Ana  /  idade = 20

  Digite 1  ->  cadastre mais um usuario
               Exemplo: nome = Bruno  /  idade = 22

  Digite 2  ->  para ver os usuarios cadastrados
               Vai aparecer Ana e Bruno na lista

  Digite 3  ->  para criar amizade
               Digite o ID 1 e depois o ID 2
               Ana e Bruno vao se tornar amigos

  Digite 4  ->  para ver as amizades
               Digite o ID 1
               Vai aparecer Bruno como amigo de Ana

  Digite 5  ->  para remover uma amizade
               Digite os IDs dos dois usuarios

  Digite 6  ->  para remover um usuario
               Digite o ID do usuario
               Confirme digitando  s  e pressionando Enter

  Digite 0  ->  para sair do programa
               Os dados serao salvos automaticamente

---

## PASSO 8 - Verificar se os dados foram salvos

Apos sair pelo menu opcao 0, abra a pasta do projeto.
Um novo arquivo chamado dados.json  vai aparecer:

    mini_rede_social/
    +-- main.py
    +-- usuarios.py
    +-- amizades.py
    +-- dados.py
    +-- README.md
    +-- dados.json    <- criado automaticamente

Esse arquivo guarda todos os usuarios e amizades cadastrados.

---

## PASSO 9 - Confirmar que os dados sao carregados

Execute o programa novamente:

    python main.py

Desta vez vai aparecer:

    Dados carregados! 2 usuario(s) encontrado(s).

Isso significa que os dados foram salvos e carregados com sucesso.
Os usuarios e amizades continuam exatamente como foram deixados.

---

## PASSO 10 - Encerrar corretamente

Para encerrar o programa, sempre use a opcao 0 do menu:

    Escolha uma opcao: 0

    Dados salvos com sucesso!
    Encerrando o sistema. Ate logo!

ATENCAO: nao feche a janela do terminal nem pressione CTRL+C
enquanto o programa estiver rodando. Se fizer isso, os dados
da sessao atual serao perdidos pois o salvamento nao sera executado.

---

## Erros comuns e como resolver

  Erro: python nao e reconhecido como comando
  Causa: Python nao esta instalado ou o PATH nao foi configurado
  Solucao: Instale o Python marcando a opcao "Add Python to PATH"

  Erro: No module named 'usuarios'
  Causa: O terminal nao esta dentro da pasta do projeto
  Solucao: Abra o terminal dentro da pasta mini_rede_social

  Erro: Dados somem ao reiniciar o programa
  Causa: O programa foi fechado sem usar a opcao 0
  Solucao: Sempre sair pelo menu digitando 0

  Erro: ModuleNotFoundError
  Causa: Algum arquivo esta em pasta diferente dos outros
  Solucao: Confirme que todos os 5 arquivos estao na mesma pasta

---

## Estrutura de dados

Cada usuario e representado por um dicionario Python:

    usuario = {
        "id": 1,
        "nome": "Mario",
        "idade": 20,
        "amigos": [2, 3]
    }

Todos os usuarios ficam armazenados em uma lista:

    usuarios = [
        {"id": 1, "nome": "Mario",   "idade": 20, "amigos": [2]},
        {"id": 2, "nome": "Bruno", "idade": 22, "amigos": [1]}
    ]

---

## Como os modulos se conectam

    main.py
      +-- importa -> dados.py      (salvar_dados, carregar_dados)
      +-- importa -> usuarios.py   (cadastrar_usuario, listar_usuarios, remover_usuario)
      +-- importa -> amizades.py   (criar_amizade, listar_amizades, remover_amizade)

    amizades.py
      +-- importa -> usuarios.py   (buscar_usuario_por_id)

---

## Observacoes

- O projeto NAO utiliza Programacao Orientada a Objetos (POO)
- Nenhuma biblioteca externa e necessaria
- Todos os arquivos devem estar na mesma pasta para funcionar
- O arquivo dados.json e criado automaticamente ao sair pelo menu opcao 0
