dia = int(input("Digite o dia: "))
mes = int(input("Digite o mês (1-12): "))
ano = int(input("Digite o ano: "))

bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

if mes < 1 or mes > 12:
    print("Data inválida.")
else:
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        dias_mes = 31
    elif mes in [4, 6, 9, 11]:
        dias_mes = 30
    else:  # Fevereiro
        dias_mes = 29 if bissexto else 28

    if 1 <= dia <= dias_mes:
        print("Data válida.")
    else:
        print("Data inválida.")