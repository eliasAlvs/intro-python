import json

def salvar_dados(caminho: str, dados: dict) -> None:
    """
    Método para salvar dados em um arquivo JSON.

    Args:
        caminho (str): caminho até o arquivo JSON.
        dados (dict): dados que precisam ser salvos no JSON.
    """
    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)

def carregar_dados(caminho: str) -> dict:
    """
        Método para buscar um usuário pelo seu cpf.

        Args:
            caminho (str): caminho até o arquivo JSON.

        Returns:
            dict: retorna um dict com os dados salvos dentro do arquivo JSON. Caso o arquivo não seja encontrado, retorna um dict vazio.
        """
    try:
        with open(caminho, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {}
