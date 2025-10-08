correta = ['B', 'C', 'D', 'A']

respostas = []
for i in range(4):
    carta = input(f"Escolha a carta {i+1} (A, B, C ou D): ").strip().upper()
    respostas.append(carta)

pontos = 0
for i in range(4):
    if respostas[i] == correta[i]:
        pontos += 10

for carta in respostas:
    if carta == 'A':
        pontos += 5

for i in range(3): 
    if respostas[i] == 'C' and respostas[i+1] == 'D':
        pontos += 5
        break 

if pontos > 50:
    pontos = 50

print(f"Sua pontuação final é: {pontos}")