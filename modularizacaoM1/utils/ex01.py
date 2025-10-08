def calcularBonus(salario: int, tempo_empresa: int) -> int:
    """
    Calcula o percentual de bônus de um funcionário com base no salário e no tempo de empresa.

    Regras:
    - Salário < 2000 e tempo de empresa >= 5 anos → bônus de 20%
    - Salário < 2000 e tempo de empresa < 5 anos → bônus de 10%
    - Salário >= 2000 e tempo de empresa >= 5 anos → bônus de 5%
    - Salário >= 2000 e tempo de empresa < 5 anos → bônus de 0%

    Args:
        salario (int): O salário atual do funcionário.
        tempo_empresa (int): O tempo de empresa em anos.

    Returns:
        int: O percentual de bônus correspondente.
    """
    if salario < 2000 and tempo_empresa >= 5:
        bonus = 20
    elif salario < 2000 and tempo_empresa < 5:
        bonus = 10
    elif salario >= 2000 and tempo_empresa >= 5:
        bonus = 5
    else:
        bonus = 0

    return bonus

def ex01() -> None:
    """
    Solicita o salário e o tempo de empresa do funcionário, calcula o bônus
    utilizando a função calcular_bonus() e exibe o resultado.

    Returns:
        None
    """
    salario = int(input("Digite o seu salário: "))
    tempo_empresa = int(input("Digite seu tempo de empresa (anos): "))
    bonus = calcularBonus(salario, tempo_empresa)
    print(f"Seu bônus é {bonus}%")
