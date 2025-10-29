class Usuario:
    def __init__(self, nome: str, cpf: str) -> None:
        """
        Método construtor de Usuario.

        Args:
            nome (str): Nome do usuário.
            cpf (str): CPF do usuário.
        """
        self.nome = nome
        self.cpf = cpf

class GerenciadorUsuarios:
    def __init__(self) -> None:
        """
        Método construtor de GerenciadorUsuarios.
        """
        self.listaUsuarios = []

    def adicionar_usuario(self, usuario: Usuario) -> None:
        """
        Método para adicionar um usuário a lista de usuários cadastrados do gerenciador (listaUsuarios).

        Args:
            usuario (Usuario): O usuário que está sendo adicionado a lista de usuários cadastrados (listaUsuarios).
        """
        self.listaUsuarios.append(usuario)

    def buscar_por_cpf(self, cpf: str) -> Usuario | None:
        """
        Método para buscar um usuário pelo seu cpf.

        Args:
            cpf (str): O CPF do usuário que está sendo procurado.

        Returns:
            Usuario: Se houver alguma correspondência do cpf passado no argumento do método com o cpf de algum usuario já cadastrado na listaUsuarios.
            None: Se não houver correspondências.
        """
        for usuario in self.listaUsuarios:
            if usuario.cpf == cpf:
                return usuario
        return None
