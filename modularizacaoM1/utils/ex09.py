def calculaPrecoFinal(vip: bool, precoProduto: float) -> float:
    """
    Calcula o preço final de um produto aplicando descontos conforme o valor e status VIP do cliente.

    Regras:
    - Clientes VIP recebem 5% de desconto adicional.
    - Produtos com preço:
        - >= 100: desconto de 20%
        - entre 50 e 99.99: desconto de 10%
        - abaixo de 50: sem desconto
    - O desconto VIP é cumulativo com o desconto por preço.

    Args:
        vip (bool): Indica se o cliente é VIP (True) ou não (False).
        precoProduto (float): Preço original do produto.

    Returns:
        float: Preço final com desconto aplicado.
    """
    if vip:
        desconto = 0.05
    else:
        desconto = 0

    if precoProduto >= 100:
        desconto += 0.2
    elif precoProduto >= 50 and precoProduto < 100:
        desconto += 0.1
    elif precoProduto < 50:
        desconto += 0
        
    return precoProduto - (precoProduto * desconto)

def ex09() -> None:
    """
    Executa o exercício 09:
    Solicita ao usuário se ele é VIP e o preço de um produto,
    calcula e exibe o valor final com desconto.

    Returns: 
        None
    """
    vip = bool(int(input("Você é um cliente VIP?(0-1)")))
    precoProduto = float(input("Digite o preço do produto: "))
    print("O preço com desconto é: " + str(calculaPrecoFinal(vip, precoProduto)))
