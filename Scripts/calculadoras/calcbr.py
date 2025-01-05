# Este script converte um valor em Reais (BRL) para todas as moedas do mundo.

import requests

def obter_taxas_de_cambio():
    """
    Obtém as taxas de câmbio para a moeda BRL usando a API ExchangeRate-API.
    
    A URL utilizada aqui consulta os preços de todas as moedas em relação ao Real (BRL).
    
    Retorna:
    dict: Um dicionário com as taxas de câmbio de todas as moedas em relação ao BRL.
    """
    # URL da API ExchangeRate-API para obter taxas de câmbio
    url = "https://api.exchangerate-api.com/v4/latest/BRL"
    resposta = requests.get(url)  # Faz a requisição GET para a API
    return resposta.json()  # Retorna a resposta em formato JSON

def converter_valor(valor, taxas):
    """
    Converte o valor fornecido em BRL para diferentes moedas usando as taxas de câmbio.
    
    Parâmetros:
    valor (float): O valor em Reais a ser convertido.
    taxas (dict): Um dicionário com as taxas de câmbio de todas as moedas.
    
    Retorna:
    dict: Um dicionário com os valores convertidos para cada moeda.
    """
    conversoes = {}
    for moeda, taxa in taxas['rates'].items():
        conversoes[moeda] = valor * taxa  # Converte o valor para cada moeda
    return conversoes

def main():
    # Solicita ao usuário o valor em Reais a ser convertido
    valor = float(input("Digite o valor em Reais (BRL) a ser convertido: "))

    # Obtém as taxas de câmbio
    taxas = obter_taxas_de_cambio()

    # Exibe as taxas de câmbio
    print(f"\nTaxas de câmbio para BRL:")
    for moeda, taxa in taxas['rates'].items():
        print(f"{moeda}: {taxa:.4f} BRL")

    # Converte o valor para as moedas
    conversoes = converter_valor(valor, taxas)

    # Exibe os resultados da conversão
    print(f"\nValor convertido de {valor} BRL:")
    for moeda, valor_convertido in conversoes.items():
        print(f"{valor_convertido:.4f} {moeda}")

if __name__ == "__main__":
    main()
