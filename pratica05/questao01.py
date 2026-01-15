"""1 - Crie uma função que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de
gorjeta desejada. Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.
Parâmetros:
a - valor_conta (float): O valor total da conta
b - porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 10 para 10%)
c - retorna: float: O valor da gorjeta calculada"""

def ler_float(mensagem: str) -> float:
    while True:
        entrada = input(mensagem).strip()
        if not entrada:
            print("Entrada vazia. Tente novamente.")
            continue
        try:
            return float(entrada.replace(",", "."))
        except ValueError:
            print("Valor inválido. Digite um número (ex.: 200 ou 200,50).")

def main():
    print("=== Cálculo de Gorjeta ===")
    valor_conta = ler_float("Informe o valor total da conta: ")
    while valor_conta < 0:
        print("O valor da conta não pode ser negativo.")
        valor_conta = ler_float("Informe o valor total da conta: ")

    porcentagem = ler_float("Informe a porcentagem da gorjeta (ex: 10 para 10%): ")
    while porcentagem < 0:
        print("A porcentagem da gorjeta não pode ser negativa.")
        porcentagem = ler_float("Informe a porcentagem da gorjeta (ex: 10 para 10%): ")

    gorjeta = valor_conta * (porcentagem / 100)
    total = valor_conta + gorjeta

    print("\n=== Resultado ===")
    print(f"Valor da gorjeta: R$ {gorjeta:.2f}")
    print(f"Total a pagar (conta + gorjeta): R$ {total:.2f}")

if __name__ == "__main__":
    main()