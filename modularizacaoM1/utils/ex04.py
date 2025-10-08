def verificarAprovacao(media: float) -> str:
    """
    Verifica a situação final do aluno com base em sua média.

    Regras:
    - Média igual a 0 → "Reprovado automático"
    - Média >= 7 → "Aprovado"
    - 5 <= Média < 7 → "Recuperação"
    - Média < 5 → "Reprovado"

    Args:
        media (float): A média final do aluno.

    Returns:
        str: A situação do aluno — "Aprovado", "Recuperação",
        "Reprovado" ou "Reprovado automático".
    """
    if media == 0:
        return "Reprovado automático"
    elif media >= 7:
        return "Aprovado"
    elif media >= 5 and media < 7:
        return "Recuperação"
    elif media < 5:
        return "Reprovado"

def ex04() -> None:
    """
    Lê as notas de três provas, calcula a média e exibe a situação final
    do aluno utilizando a função verificarAprovacao().

    Fórmula:
        média = (n1 + n2 + n3) / 3

    Returns:
        None
    """
    n1 = float(input("Digite a nota da primeira prova: "))
    n2 = float(input("Digite a nota da segunda prova: "))
    n3 = float(input("Digite a nota da terceira prova: "))
    media = (n1 + n2 + n3) / 3
    print(verificarAprovacao(media))
    
