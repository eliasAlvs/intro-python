from usuario import *
from livro import *
from emprestimo import *
from persistencia import *

def exibir_menu() -> str:
    """
    Função para exibir o menu de opções e retorna uma opção.

    Returns:
        str: retorna a opção escolhida.
    """
    print("\n---- SISTEMA DE BIBLIOTECA ----")
    print("1. Cadastrar livro")
    print("2. Cadastrar usuário")
    print("3. Emprestar livro")
    print("4. Devolver livro")
    print("5. Consultar livros")
    print("6. Listar empréstimos de um usuário")
    print("0. Sair e salvar")
    return input("Escolha uma opção: ")

def opcao1() -> None:
    """
    Função para receber os dados do livro e realizar o seu cadastro.
    """
    print("\n------ CADASTRO DE LIVRO ------")
    titulo = input("Título: ")
    autor = input("Autor: ")
    anoPublicacao = int(input("Ano de Publicação: "))
    nExemplares = int(input("Número de Exemplares: "))
    gerenciador_livros.cadastrar_livro(Livro(titulo, autor, anoPublicacao, nExemplares))
    print("✅LIVRO CADASTRADO✅")

def opcao2() -> None:
    """
    Função para receber os dados do usuário e realizar o seu cadastro.
    """
    print("\n----- CADASTRO DE USUÁRIO -----")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    gerenciador_usuarios.adicionar_usuario(Usuario(nome, cpf))
    print("✅USUÁRIO CADASTRADO✅")

def opcao3() -> None:
    """
    Função para receber os dados do usuário e livro e realizar um emprestimo.
    """
    print("\n------- EMPRESTAR LIVRO -------")
    cpf = input("CPF do Usuário: ")
    titulo = input("Título do Livro: ")
    usuario = gerenciador_usuarios.buscar_por_cpf(cpf)
    livro = gerenciador_livros.buscar_por_titulo(titulo)
    if usuario and livro:
        if gerenciador_emprestimos.emprestar_livro(usuario, livro):
            print("✅EMPRÉSTIMO CONCLUÍDO✅")
        else:
            print("❌LIVRO INDISPONÍVEL❌")
    else:
        print("❌USUÁRIO OU LIVRO NÃO ENCONTRADO❌")

def opcao4() -> None:
    """
    Função para receber os dados de um usuário e livro e realizar devolução do livro.
    """
    print("\n------- DEVOLVER LIVRO --------")
    cpf = input("CPF do usuário: ")
    titulo = input("Título do livro: ")
    usuario = gerenciador_usuarios.buscar_por_cpf(cpf)
    if gerenciador_emprestimos.devolver_livro(usuario, titulo):
        print("✅LIVRO DEVOLVIDO✅")
    else:
        print("❌NÃO FOI POSSÍVEL DEVOLVER O LIVRO❌")

def opcao5() -> None:
    """
    Função para receber titulo ou nome de um autor de um livro e realizar a sua busca.
    """
    print("\n------- CONSULTAR LIVROS ------")
    tituloOuAutor = input("Digite o título ou Autor:")
    livro_consultado = gerenciador_livros.consultar_livro(tituloOuAutor)
    if livro_consultado:
        i = 1
        for livro in livro_consultado:
            print(f"\nLivro: {i}")
            print(f"\tTítulo: {livro.titulo}")
            print(f"\tAutor: {livro.autor}")
            print(f"\tAno de Publicação: {livro.anoPublicacao}")
            print(f"\tExemplares disponíveis: {livro.nExemplares}")
            i+=1
        print("✅ LIVROS CONSULTADOS ✅")
    else:
        print("❌NENHUM LIVRO ENCONTRADO❌")

def opcao6() -> None:
    """
    Função para listar os empréstimos de um usuário.
    """
    print("\n------- LISTAR EMPRÉSTIMO DE UM USUÁRIO -------")
    cpf = input("CPF do usuário: ")
    usuario = gerenciador_usuarios.buscar_por_cpf(cpf)
    if usuario:
        emprestimos = gerenciador_emprestimos.listar_emprestimos_usuario(usuario)
        print(f"✅EMPRÉSTIMOS ATIVOS DE {usuario.nome}✅: ")
        for emprestimo in emprestimos:
            print(f"- {emprestimo}")
    else:
        print("❌USUÁRIO NÃO ENCONTRADO❌")
    
def opcao0() -> dict:
    """
    Função para sair e salvar os dados cadastrados no sistema.

    Returns:
        dict: retorna o dicionário de dados dos livros, usuarios e emprestimos.
    """
    print("\n------- SAIR E SALVAR -------")
    dados = {
        "livros": [
            {"titulo": l.titulo, "autor": l.autor, "anoPublicacao": l.anoPublicacao, "nExemplares": l.nExemplares}
            for l in gerenciador_livros.listaLivros
        ],
        "usuarios": [
            {"nome": u.nome, "cpf": u.cpf}
            for u in gerenciador_usuarios.listaUsuarios
        ],
        "emprestimos": [
            {"usuario": e.usuario.cpf, "livro": e.livro.titulo}
            for e in gerenciador_emprestimos.listaEmprestimos
        ]
    }
    print("✅DADOS SALVOS COM SUCESSO. FIM DO PROGRAMA✅")
    return dados

CAMINHO_ARQUIVO = "Faculdade/biblioteca/biblioteca.json"
dados = carregar_dados(CAMINHO_ARQUIVO)
usuarios_salvos = dados.get("usuarios", [])
livros_salvos = dados.get("livros", [])
emprestimos_salvos = dados.get("emprestimos", [])
gerenciador_usuarios = GerenciadorUsuarios()
gerenciador_livros = GerenciadorLivros()
gerenciador_emprestimos = GerenciadorEmprestimos()

for usuario in usuarios_salvos:
    gerenciador_usuarios.adicionar_usuario(Usuario(usuario["nome"], usuario["cpf"]))

for livro in livros_salvos:
    gerenciador_livros.cadastrar_livro(Livro(livro["titulo"], livro["autor"], livro["anoPublicacao"], livro["nExemplares"]))

for emprestimo in emprestimos_salvos:
    usuario = gerenciador_usuarios.buscar_por_cpf(emprestimo["usuario"])
    livro = gerenciador_livros.buscar_por_titulo(emprestimo["livro"])
    if usuario and livro:
        gerenciador_emprestimos.listaEmprestimos.append(Emprestimo(usuario, livro))

while True:
    opcao = exibir_menu()
    if opcao == "1": # Cadastrar livro
        opcao1()
    elif opcao == "2": # Cadastrar usuário
        opcao2()
    elif opcao == "3": # Emprestrar livro
        opcao3()
    elif opcao == "4": # Devolver livro
        opcao4()
    elif opcao == "5": # Consultar livros
        opcao5()
    elif opcao == "6": # Listar empréstimos de um usuário
        opcao6()
    elif opcao == "0": # Sair e salvar
        dados = opcao0()
        salvar_dados(CAMINHO_ARQUIVO, dados)
        break
    else: 
        print("Opção inválida!")
        


