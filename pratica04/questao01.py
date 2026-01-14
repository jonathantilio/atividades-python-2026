#1 - Criar um código que faça uma calculadora que tenha as operações básicas(+,-,*,/).

def calculadora():
    print("=== Calculadora Básica ===")
    print("Operações disponíveis: +  -  *  /")

    num1 = float(input("Digite o primeiro número: "))
    operacao = input("Digite a operação (+, -, *, /): ")
    num2 = float(input("Digite o segundo número: "))

    if operacao == "+":
        resultado = num1 + num2
    elif operacao == "-":
        resultado = num1 - num2
    elif operacao == "*":
        resultado = num1 * num2
    elif operacao == "/":
        if num2 != 0:
            resultado = num1 / num2
        else:
            return "Erro: divisão por zero não é permitida!"
    else:
        return "Operação inválida!"

    return f"Resultado: {resultado}"

print(calculadora())