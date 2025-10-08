def verificarPeso(imc: float) -> str:
    """
    Classifica o peso corporal de uma pessoa com base no valor do IMC (Índice de Massa Corporal).

    Faixas de classificação:
    - IMC < 18.5 → Abaixo do peso
    - 18.5 <= IMC < 25 → Peso normal
    - 25 <= IMC < 30 → Sobrepeso
    - 30 <= IMC < 35 → Obesidade grau I
    - 35 <= IMC < 40 → Obesidade grau II
    - IMC >= 40 → Obesidade grau III

    Args:
        imc (float): Valor do índice de massa corporal calculado.

    Returns:
        str: Classificação correspondente ao IMC.
    """
    if imc < 18.5:
        return "Abaixo do peso"
    elif imc >= 18.5 and imc <25:
        return "Peso normal"
    elif imc >= 25 and imc < 30:
        return "Sobrepeso"
    elif imc >= 30 and imc < 35:
        return "Obesidade grau I"
    elif imc >= 35 and imc < 40:
        return "Obesidade grau II"
    elif imc >= 40:
        return "Obesidade grau III"

def ex03() -> None:
    """
    Lê o peso e a altura do usuário, calcula o IMC e exibe a classificação
    correspondente utilizando a função verificarPeso().

    Fórmula:
        IMC = peso / (altura ** 2)

    Obs:
        A altura deve ser informada em centímetros.

    Returns:
        None
    """
    peso = float(input("Digite o seu peso: "))
    altura = float(input("Digite a sua altura (em cm): ")) / 100

    imc = peso / (altura * altura)
    print(verificarPeso(imc))