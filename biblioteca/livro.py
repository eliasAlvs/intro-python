class Livro:
    def __init__(self, titulo: str, autor: str, anoPublicacao: int, nExemplares: int):
        self.titulo = titulo
        self.autor = autor
        self.anoPublicacao = anoPublicacao
        self.nExemplares = nExemplares


class GerenciadorLivros:
    def __init__(self):
        self.listaLivros = []

    def cadastrar_livro(self, livro):
        self.listaLivros.append(livro)

    def consultar_livro(self, tituloOuAutor):
        return [
            livro
            for livro in self.listaLivros
            if tituloOuAutor.lower() in livro.titulo.lower()
            or tituloOuAutor.lower() in livro.autor.lower()
        ]
    
    def buscar_por_titulo(self, titulo: str):
        for livro in self.listaLivros:
            if livro.titulo.lower() == titulo.lower():
                return livro
        return None
