"""4 - Crie um programa que realize consultas a cotações de moedas em relação ao Real (BRL) usando a API AwesomeAPI, mostre valor atual, máxima, mínima e data/hora da última atualização, caso a moeda não existir ou houver erro na requisição, retorne uma mensagem de erro"""

import requests

def consultar_cotacao(moeda: str):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    try:
        resposta = requests.get(url, timeout=5)
        resposta.raise_for_status()
        dados = resposta.json()

        chave = f"{moeda}BRL"
        if chave not in dados:
            print("Moeda não encontrada na API.")
            return

        info = dados[chave]
        valor_atual = info.get("bid", "N/A")
        maxima = info.get("high", "N/A")
        minima = info.get("low", "N/A")
        atualizacao = info.get("create_date", "N/A")

        print("\n=== Resultado da Consulta ===")
        print(f"Moeda: {moeda}/BRL")
        print(f"Valor atual: R$ {valor_atual}")
        print(f"Máxima: R$ {maxima}")
        print(f"Mínima: R$ {minima}")
        print(f"Última atualização: {atualizacao}")

    except requests.exceptions.RequestException:
        print("Falha na conexão com a API AwesomeAPI.")

def main():
    print("=== Consulta de Cotação de Moedas ===")
    moeda = input("Digite o código da moeda (ex: USD, EUR, BTC): ").strip().upper()
    consultar_cotacao(moeda)

if __name__ == "__main__":
    main()