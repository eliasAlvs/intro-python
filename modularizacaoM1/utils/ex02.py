a = float(input("Digite o primeiro lado: "))
b = float(input("Digite o segundo lado: "))
c = float(input("Digite o terceiro lado: "))

if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Formam um triângulo: equilátero.")
    elif a == b or b == c or a == c:
        print("Formam um triângulo: isósceles.")
    else:
        print("Formam um triângulo: escaleno.")
else:
    print("Os valores informados NÃO formam um triângulo.")
