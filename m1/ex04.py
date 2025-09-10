n1 = float(input("Digite a nota da primeira prova: "))
n2 = float(input("Digite a nota da segunda prova: "))
n3 = float(input("Digite a nota da terceira prova: "))
media = (n1 + n2 + n3) / 3

if media == 0:
    print("Reprovado automático")
elif media >= 7:
    print("Aprovado")
elif media >= 5 and media < 7:
    print("Recuperação")
elif media < 5:
    print("Reprovado")
    