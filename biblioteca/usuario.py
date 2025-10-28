class Usuario:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class GerenciadorUsuarios:
    def __init__(self):
        self.listaUsuarios = []

    def adicionar_usuario(self, usuario):
        self.listaUsuarios.append(usuario)

    def buscar_por_cpf(self, cpf):
        for usuario in self.listaUsuarios:
            if usuario.cpf == cpf:
                return usuario
        return None
