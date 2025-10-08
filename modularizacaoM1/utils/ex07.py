def calculaRisco(renda: float, dividas: float) -> str:
    """
    Avalia o nível de risco financeiro de uma pessoa com base em sua renda mensal
    e no valor total de suas dívidas.

    O risco é determinado pelas seguintes regras:
    - Renda < 2000 e percentual de dívida > 50% → Risco "Alta"
    - 2000 <= Renda <= 5000 ou 30% <= percentual de dívida <= 50% → Risco "Média"
    - Renda > 5000 e percentual de dívida < 30% → Risco "Baixa"
    - Qualquer outro caso → Risco "Médio-baixo"

    Args:
        renda (float): Renda mensal do usuário.
        dividas (float): Valor total das dívidas do usuário.

    Returns:
        str: Classificação do risco — "Alta", "Média", "Baixa" ou "Médio-baixo".
    """
    if renda > 0:
        percentualDivida = (dividas / renda) * 100
    else:
        percentualDivida = 100  

    if renda < 2000 and percentualDivida > 50:
        risco = "Alta"
    elif (2000 <= renda <= 5000) or (30 <= percentualDivida <= 50):
        risco = "Média"
    elif renda > 5000 and percentualDivida < 30:
        risco = "Baixa"
    else:
        risco = "Médio-baixo"

    return risco

def ex07() -> None:
    """
    Lê a idade, renda mensal e valor total das dívidas do usuário,
    calcula o nível de risco financeiro e exibe o resultado.

    Returns:
        None
    """
    idade = int(input("Digite sua idade: "))
    renda = float(input("Digite sua renda mensal: "))
    dividas = float(input("Digite o valor total de suas dívidas: "))
    print(f"Risco: " + calculaRisco(renda, dividas))