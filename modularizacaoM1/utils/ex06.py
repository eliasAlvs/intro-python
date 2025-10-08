def verificaVoto(idade: int, nacionalidade: int) -> str:
    """
    Determina a obrigatoriedade do voto de uma pessoa com base na idade e na nacionalidade.

    Regras:
    - Brasileiros com idade entre 16 e 17 anos → voto opcional
    - Brasileiros com 18 anos ou mais → voto obrigatório
    - Estrangeiros de qualquer idade → voto opcional

    Args:
        idade (int): Idade da pessoa.
        nacionalidade (int): Código da nacionalidade (1 = Brasileiro, 2 = Estrangeiro).

    Returns:
        str: Situação do voto — "Voto obrigatório" ou "Voto opcional".
    """
    if idade >= 16 and idade < 18:
        return "Voto opcional"
    else:
        if nacionalidade == 1:
            return "Voto obrigatório"
        else:
            return "Voto opcional"
        
def ex06() -> None:
    """
    Solicita a idade e a nacionalidade do usuário, verifica a obrigatoriedade do voto
    utilizando a função verificaVoto(), e exibe o resultado.

    Returns:
        None
    """
    idade = int(input("Digite sua idade: "))
    nacionalidade = int(input("NACIONALIDADE: \nBrasileiro(1) \nEstrangeiro(2)"))
    print(verificaVoto(idade, nacionalidade))
