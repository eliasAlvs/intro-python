import utils

continuar = True
while continuar:
    opcao = int(input("Escolha uma opção(1-10): "))
    match opcao:
        case 1:
            utils.ex01()
        case 2:
            utils.ex02()
        case 3:
            utils.ex03()
        case 4:
            utils.ex04()
        case 5:
            utils.ex05()
        case 6:
            utils.ex06()
        case 7:
            utils.ex07()
        case 8:
            utils.ex08()
        case 9:
            utils.ex09()
        case 10:
            utils.ex10()
        case _:
            print("Digite uma opção válida(1-10)!")
            continue
        
    continuar = bool(int(input("Você deseja continuar? (Não = 0 / Sim = 1)")))

