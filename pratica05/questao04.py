"""4 - Crie um programa que calcule a quantos dias um individuo está vivo de acordo com a data do dia."""

from datetime import datetime

def main():
    print("=== Calculadora de Dias de Vida ===")
    data_nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ").strip()

    try:
        nascimento = datetime.strptime(data_nascimento, "%d/%m/%Y")
        hoje = datetime.today()
        dias_vividos = (hoje - nascimento).days

        print(f"\nVocê está vivo há {dias_vividos} dias.")
    except ValueError:
        print("Formato inválido. Use o formato dd/mm/aaaa.")

if __name__ == "__main__":
    main()