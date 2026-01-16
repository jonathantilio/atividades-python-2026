"""1 - Crie um programa que gere senhas aleatórias com letras, números e símbolos e que o usuário  também escolha o tamanho da senha  para criar senhas seguras automaticamente."""

import random
import string

def gerar_senha(tamanho: int) -> str:
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def main():
    print("=== Gerador de Senhas Aleatórias ===")
    try:
        tamanho = int(input("Digite o tamanho da senha desejada: "))
        if tamanho <= 0:
            print("O tamanho deve ser maior que zero.")
            return
        senha = gerar_senha(tamanho)
        print(f"\nSua senha gerada é: {senha}")
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")

if __name__ == "__main__":
    main()