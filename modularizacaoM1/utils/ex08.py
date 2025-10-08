def calculaPontos(respostas: list[str]) -> int:
    """
    Calcula a pontuação de um jogador com base nas respostas dadas.

    Regras:
    - Cada resposta correta (posição certa e letra certa) vale 10 pontos.
    - Cada carta 'A' dá 5 pontos extras.
    - Se houver uma sequência 'C' seguida de 'D', ganha mais 5 pontos.
    - A pontuação máxima é 50.

    Args:
        respostas (list[str]): Lista contendo 4 letras ('A', 'B', 'C' ou 'D').

    Returns:
        int: Pontuação final, limitada a 50 pontos.
    """
    correta = ['B', 'C', 'D', 'A']
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

    if pontos > 50:
        pontos = 50
    return pontos

def ex08() -> None:
    """
    Executa o exercício 08:
    Solicita 4 respostas ao usuário, calcula e exibe a pontuação final.

    Returns:
        None
    """
    respostas = []
    for i in range(4):
        carta = input(f"Escolha a carta {i+1} (A, B, C ou D): ").strip().upper()
        respostas.append(carta)
    print("Sua pontuação final é: " + str(calculaPontos(respostas)))