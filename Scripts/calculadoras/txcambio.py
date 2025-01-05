import requests

def obter_taxas_de_cambio(moeda_base):
    """
    Obtém as taxas de câmbio para a moeda base usando a API CoinGecko.
    
    A API CoinGecko fornece informações sobre preços de criptomoedas em relação a moedas fiat.
    A URL utilizada aqui consulta os preços de Bitcoin, Ethereum, Ripple e Litecoin em relação
    à moeda base fornecida pelo usuário.
    
    Parâmetros:
    moeda_base (str): A moeda em que as taxas de câmbio serão retornadas (ex: 'usd', 'brl', 'eur').
    
    Retorna:
    dict: Um dicionário com as taxas de câmbio das criptomoedas em relação à moeda base.
    """
    # URL da API CoinGecko para obter preços de criptomoedas
    url = f"https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,ripple,litecoin&vs_currencies={moeda_base}"
    resposta = requests.get(url)  # Faz a requisição GET para a API
    return resposta.json()  # Retorna a resposta em formato JSON

def converter_valor(valor, taxas):
    """
    Converte o valor fornecido para diferentes criptomoedas usando as taxas de câmbio.
    
    Parâmetros:
    valor (float): O valor a ser convertido.
    taxas (dict): Um dicionário com as taxas de câmbio das criptomoedas.
    
    Retorna:
    dict: Um dicionário com os valores convertidos para cada criptomoeda.
    """
    conversoes = {}
    for cripto, dados in taxas.items():
        conversoes[cripto] = valor * dados  # Converte o valor para cada criptomoeda
    return conversoes

def main():
    # Solicita ao usuário a moeda base e o valor a ser convertido
    moeda_base = input("Digite a moeda base (ex: usd, brl, eur): ").strip().lower()
    valor = float(input("Digite o valor a ser convertido: "))

    # Obtém as taxas de câmbio
    taxas = obter_taxas_de_cambio(moeda_base)

    # Exibe as taxas de câmbio
    print(f"\nTaxas de câmbio para {moeda_base.upper()}:")
    for cripto, dados in taxas.items():
        print(f"{cripto.capitalize()}: {dados[moeda_base]} {moeda_base.upper()}")

    # Converte o valor para as criptomoedas
    conversoes = converter_valor(valor, taxas)

    # Exibe os resultados da conversão
    print(f"\nValor convertido de {valor} {moeda_base.upper()}:")
    for cripto, valor_convertido in conversoes.items():
        print(f"{valor_convertido:.6f} {cripto.capitalize()}")

if __name__ == "__main__":
    main()
