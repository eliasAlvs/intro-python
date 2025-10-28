from usuario import *
from livro import *
class Emprestimo:
    def __init__(self, usuario: Usuario, livro: Livro):
        self.usuario = usuario
        self.livro = livro

class GerenciadorEmprestimos:
    def __init__(self):
        self.listaEmprestimos = []

    def emprestar_livro(self, usuario: Usuario, livro: Livro) -> bool:
        if livro.nExemplares > 0:
            livro.nExemplares -= 1
            self.listaEmprestimos.append(Emprestimo(usuario, livro))
            return True
        return False
    
    def devolver_livro(self, usuario, titulo):
        for emprestimo in self.listaEmprestimos:
            if emprestimo.usuario == usuario and emprestimo.livro.titulo.lower() == titulo.lower():
                emprestimo.livro.nExemplares += 1
                self.listaEmprestimos.remove(emprestimo)
                return True
        return False
        
    def listar_emprestimos_usuario(self, usuario):
        return [e.livro.titulo for e in self.listaEmprestimos if e.usuario == usuario]