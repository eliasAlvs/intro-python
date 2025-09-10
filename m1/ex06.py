idade = int(input("Digite sua idade: "))
nacionalidade = int(input("NACIONALIDADE: \nBrasileiro(1) \nEstrangeiro(2)"))

if idade >= 16 and idade < 18:
    print("Voto opcional")
else:
    if nacionalidade == 1:
        print("Voto obrigatório")
    else:
        print("Voto opcional")