salario = int(input("Digite o seu salário: "))
tempoEmpresa = int(input("Digite seu tempo de empresa (anos): "))

if salario < 2000 and tempoEmpresa >= 5:
    bonus = 20
elif salario < 2000 and tempoEmpresa < 5:
    bonus = 10
elif salario >= 2000 and tempoEmpresa >= 5:
    bonus = 5
elif salario >= 2000 and tempoEmpresa < 5:
    bonus = 0

print("Seu bonus é ", bonus, "%")