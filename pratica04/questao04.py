"""4 - Criar um código que serve para analisar números digitados pelo usuário, classificando-os como pares ou ímpares e contabilizando quantos de cada tipo foram inseridos."""

def analisar_numeros():
    print("=== Analisador de Números ===")
    
    qtd = int(input("Quantos números deseja inserir? "))
    
    pares = 0
    impares = 0
    
    for i in range(qtd):
        num = int(input(f"Digite o número {i+1}: "))
        
        if num % 2 == 0:
            print(f"{num} é PAR")
            pares += 1
        else:
            print(f"{num} é ÍMPAR")
            impares += 1
    
    print("\n=== Resultado da Análise ===")
    print(f"Total de números pares: {pares}")
    print(f"Total de números ímpares: {impares}")

analisar_numeros()