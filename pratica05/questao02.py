"""2-  Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente, ignorando espaços e pontuação). Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”.
"""

def verificar_palindromo(texto: str) -> str:
    texto_limpo = ''.join(char.lower() for char in texto if char.isalnum())
    if texto_limpo == texto_limpo[::-1]:
        return "Sim"
    else:
        return "Não"

def main():
    print("=== Verificador de Palíndromo ===")
    entrada = input("Digite uma palavra ou frase: ")
    resultado = verificar_palindromo(entrada)
    print(f"É palíndromo? {resultado}")

if __name__ == "__main__":
    main()