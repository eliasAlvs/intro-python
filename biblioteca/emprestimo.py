from usuario import *
from livro import *
class Emprestimo:
    def __init__(self, usuario: Usuario, livro: Livro) -> None:
        """
        Método Construtor de um Emprestimo

        Args:
            usuario (Usuario): O usuário que está fazendo o empréstimo.
            livro (Livro): O livro que está sendo emprestado.
        """
        self.usuario = usuario
        self.livro = livro

class GerenciadorEmprestimos:
    def __init__(self) -> None:
        """
        Método Construtor do GerenciadorEmprestimos
        """
        self.listaEmprestimos = []

    def emprestar_livro(self, usuario: Usuario, livro: Livro) -> bool:
        """
        Método para um usuário emprestar um livro
        Args:
            usuario (Usuario): O usuário que está fazendo o empréstimo.
            livro (Livro): O livro que está sendo emprestado.

        Returns:
            bool: True se o número de exemplares do livro for maior que 0. Caso contrário, retorna False.
        """
        if livro.nExemplares > 0:
            livro.nExemplares -= 1
            self.listaEmprestimos.append(Emprestimo(usuario, livro))
            return True
        return False
    
    def devolver_livro(self, usuario: Usuario, titulo: str) -> bool:
        """
        Método para um usuário devolver um livro.
        Procura um empréstimo correspondente e, se encontrado, incrementa os exemplares
        e remove o empréstimo da lista.

        Args:
            usuario (Usuario): O usuário que está devolvendo o livro.
            titulo (str): O título do livro que está sendo devolvido.

        Returns:
            bool: True se o usuário e título do livro passados como argumento, tenham correspondência a algum emprestimo da listaEmprestimos. Caso contrário, retorna False.
        """
        for emprestimo in self.listaEmprestimos:
            if emprestimo.usuario == usuario and emprestimo.livro.titulo.lower() == titulo.lower():
                emprestimo.livro.nExemplares += 1
                self.listaEmprestimos.remove(emprestimo)
                return True
        return False
        
    def listar_emprestimos_usuario(self, usuario: Usuario) -> list[str]:
        """
        Método para listar todos os emprestimos ativos de um usuario.

        Args:
            usuario (Usuario): O usuário cujos emprestimos estão sendo consultados.

        Returns:
            list[str]: Retorna uma lista com os títulos dos livros que o usuario pegou emprestado e ainda não devolveu.
        """
        return [e.livro.titulo for e in self.listaEmprestimos if e.usuario == usuario]