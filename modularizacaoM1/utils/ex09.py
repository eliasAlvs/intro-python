vip = bool(int(input("Você é um cliente VIP?(0-1)")))
precoProduto = float(input("Digite o preço do produto: "))

if vip:
    desconto = 0.05
else:
    desconto = 0

if precoProduto >= 100:
    desconto += 0.2
elif precoProduto >= 50 and precoProduto < 100:
    desconto += 0.1
elif precoProduto < 50:
    desconto += 0

precoFinal = precoProduto - (precoProduto * desconto)
print(f"O preço com desconto é: {precoFinal}")
