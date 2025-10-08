def validaSenha(senha: str) -> str:
    """
    Valida se uma senha atende aos critérios de segurança.

    Critérios:
    - Mínimo de 8 caracteres
    - Contém pelo menos uma letra maiúscula
    - Contém pelo menos uma letra minúscula
    - Contém pelo menos um dígito
    - Contém pelo menos um dos símbolos: ! @ # $ %

    Args:
        senha (str): Senha a ser validada.

    Returns:
        str: "Senha válida" se atender a todos os critérios,
             caso contrário, "Senha inválida!".
    """
    simbolos = "!@#$%"

    if len(senha) >= 8 and any(c.isupper() for c in senha) and any(c.islower() for c in senha) and any(c.isdigit() for c in senha) and any(c in simbolos for c in senha):
        return "Senha válida"
    else:
        return "Senha inválida!"

def ex10() -> None:
    """
    Executa o exercício 10:
    Solicita uma senha ao usuário, verifica se é válida usando validaSenha(),
    e exibe o resultado.

    Returns:
        None
    """
    senha = input("Digite uma senha: ")
    print(validaSenha(senha))