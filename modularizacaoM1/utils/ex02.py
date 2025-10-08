def verificarTriangulo(a: float, b: float, c: float) -> str:
    """
    Verifica o tipo de triângulo com base nos comprimentos dos três lados informados.

    Regras:
    - Um triângulo é válido se todos os lados forem maiores que zero e a soma de
      dois lados for sempre maior que o terceiro.
    - Se os três lados forem iguais → Triângulo Equilátero
    - Se dois lados forem iguais → Triângulo Isósceles
    - Se todos os lados forem diferentes → Triângulo Escaleno

    Args:
        a (float): Comprimento do primeiro lado.
        b (float): Comprimento do segundo lado.
        c (float): Comprimento do terceiro lado.

    Returns:
        str: Tipo do triângulo — "equilátero", "isósceles", "escaleno" ou "inválido".
    """
    if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
        if a == b == c:
            triangulo = "equilátero"
        elif a == b or b == c or a == c:
            triangulo = "isósceles"
        else:
            triangulo = "escaleno"
    else:
            triangulo = "inválido"
    return triangulo

def ex02() -> None:
    """
    Lê os comprimentos dos três lados de um triângulo, determina seu tipo
    utilizando a função verificarTriangulo() e exibe o resultado.

    Returns:
        None
    """
    a = float(input("Digite o primeiro lado: "))
    b = float(input("Digite o segundo lado: "))
    c = float(input("Digite o terceiro lado: "))
    print("Triangulo " + verificarTriangulo(a, b, c))

