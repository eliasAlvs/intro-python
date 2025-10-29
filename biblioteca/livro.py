class Livro:
    def __init__(self, titulo: str, autor: str, anoPublicacao: int, nExemplares: int) -> None:
        """
        Método construtor do Livro.

        Args:
            titulo (str): Título do livro.
            autor (str): Autor do livro.
            anoPublicacao (int): Ano de publicacao do livro.
            nExemplares (int): Número de exemplares disponíveis do livro.
        """
        self.titulo = titulo
        self.autor = autor
        self.anoPublicacao = anoPublicacao
        self.nExemplares = nExemplares


class GerenciadorLivros:
    def __init__(self) -> None:
        """
        Método construtor do GerenciadorLivros.
        """
        self.listaLivros = []

    def cadastrar_livro(self, livro: Livro) -> None:
        """
        Método para adicionar um livro à lista de livros cadastrados.

        Args:
            livro (Livro): Livro que está sendo cadastrado no sistema.
        """
        self.listaLivros.append(livro)

    def consultar_livro(self, tituloOuAutor: str) -> list[object]:
        """
        Método para consultar livros, por autor ou título.

        Args:
            tituloOuAutor (str): O título ou nome do Autor que você quer consultar os livros.

        Returns:
            list[object]: Retorna uma lista com todos os livros da listaLivros cadastrados, que possuam correspondência com o tituloOuAutor, passado como argumento da função.
        """
        return [
            livro
            for livro in self.listaLivros
            if tituloOuAutor.lower() in livro.titulo.lower()
            or tituloOuAutor.lower() in livro.autor.lower()
        ]
    
    def buscar_por_titulo(self, titulo: str) -> Livro | None:
        """
        Método para buscar um livro, especificamente pelo título.

        Args:
            titulo (str): O título do livro que está sendo buscado.

        Returns:
            Livro: retorna um objeto da classe livro, caso o titulo passado como argumento tenha correspondência com algum dos livros dentro da listaLivros cadastrados. 
            None: Caso não haja correspondências.
        """
        for livro in self.listaLivros:
            if livro.titulo.lower() == titulo.lower():
                return livro
        return None
