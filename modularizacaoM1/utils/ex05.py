def verificarBissexto(dia: int, mes: int, ano: int) -> str:
    """
    Verifica se uma data é válida considerando os meses do ano e se o ano é bissexto.

    Um ano é considerado bissexto se:
        - For divisível por 4 e não por 100, ou
        - For divisível por 400.

    A função também valida:
        - Mês entre 1 e 12.
        - Dia dentro do intervalo permitido para o mês correspondente.

    Args:
        dia (int): Dia da data informada.
        mes (int): Mês da data informada (1 a 12).
        ano (int): Ano da data informada.

    Returns:
        str: "Data válida." se a data existir, ou "Data inválida." caso contrário.
    """
    bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
    if mes < 1 or mes > 12:
        return "Data inválida."
    else:
        if mes in [1, 3, 5, 7, 8, 10, 12]:
            dias_mes = 31
        elif mes in [4, 6, 9, 11]:
            dias_mes = 30
        else: 
            dias_mes = 29 if bissexto else 28

        if 1 <= dia <= dias_mes:
            return "Data válida."
        return "Data inválida"

def ex05() -> None:
    """
    Solicita ao usuário uma data (dia, mês e ano), verifica se ela é válida
    considerando os anos bissextos, e exibe o resultado.

    Returns:
        None
    """
    dia = int(input("Digite o dia: "))
    mes = int(input("Digite o mês (1-12): "))
    ano = int(input("Digite o ano: "))
    print(verificarBissexto(dia, mes, ano))