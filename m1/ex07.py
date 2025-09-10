idade = int(input("Digite sua idade: "))
renda = float(input("Digite sua renda mensal: "))
dividas = float(input("Digite o valor total de suas dívidas: "))

if renda > 0:
    percentualDivida = (dividas / renda) * 100
else:
    percentualDivida = 100  

if renda < 2000 and percentualDivida > 50:
    risco = "Alta"
elif (2000 <= renda <= 5000) or (30 <= percentualDivida <= 50):
    risco = "Média"
elif renda > 5000 and percentualDivida < 30:
    risco = "Baixa"
else:
    risco = "Médio-baixo"

# Saída
print(f"Risco: {risco}")