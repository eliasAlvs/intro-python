import utils

continuar = True
while continuar:
    opcao = int(input("Escolha uma opção(1-10): "))
    match opcao:
        case 1:
            ex01()
        case 2:
            ex02()
        case 3:
            ex03()
        case 4:
            ex04()
        case 5:
            ex05()
        case 6:
            ex06()
        case 7:
            ex07()
        case 8:
            ex08()
        case 9:
            ex09()
        case 10:
            ex10()
        case _:
            print("Digite uma opção válida (1-10)!")
            continue

    continuar = bool(input("Você deseja continuar? (Não = 0 / Sim = 1)"))

