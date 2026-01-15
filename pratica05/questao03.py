"""3 - Crie um programa que serve para calcular o preço final de um produto após aplicar um desconto percentual.
a - Cálculo de desconto: Calcula o valor do desconto baseado em uma porcentagem.
b - Preço final: Determina o novo preço após o desconto.
c - Formatação: Arredonda o resultado para 2 casas decimais (centavos).
d - Interação com usuário: Pede os valores necessários e mostra o resultado formatado."""

def ler_float(mensagem: str) -> float:
    while True:
        entrada = input(mensagem).strip()
        if not entrada:
            print("Entrada vazia. Tente novamente.")
            continue
        try:
            return float(entrada.replace(",", "."))
        except ValueError:
            print("Valor inválido. Digite um número (ex.: 100 ou 100,50).")

def main():
    print("=== Cálculo de Preço com Desconto ===")
    preco = ler_float("Informe o preço do produto: ")
    while preco < 0:
        print("O preço não pode ser negativo.")
        preco = ler_float("Informe o preço do produto: ")

    desconto = ler_float("Informe a porcentagem de desconto (ex: 20 para 20%): ")
    while desconto < 0:
        print("A porcentagem de desconto não pode ser negativa.")
        desconto = ler_float("Informe a porcentagem de desconto (ex: 20 para 20%): ")

    valor_desconto = preco * (desconto / 100)
    preco_final = preco - valor_desconto

    print("\n=== Resultado ===")
    print(f"Valor do desconto: R$ {valor_desconto:.2f}")
    print(f"Preço final com desconto: R$ {preco_final:.2f}")

if __name__ == "__main__":
    main()