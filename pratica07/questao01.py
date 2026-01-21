"""1 - Crie um programa que cria um arquivo CSV com nome, idade e cidade de algumas pessoas, que este programa escreva os dados em formato tabular e salva no arquivo escolhido pelo usuário, caso ocorra um erro ao salvar, mostre uma mensagem de falha. 
"""

import csv

# Lista de listas com dados fictícios
pessoas = [
    ["Nome", "Idade", "Cidade"],  # Cabeçalho
    ["Ana", 25, "Rio de Janeiro"],
    ["Carlos", 30, "São Paulo"],
    ["Mariana", 22, "Belo Horizonte"]
]

try:
    # Solicita o nome do arquivo
    nome_arquivo = input("Digite o nome do arquivo CSV para salvar: ")

    # Abre o arquivo para escrita
    with open(nome_arquivo, mode="w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerows(pessoas)  # Escreve todas as linhas

    print(f"✅ Dados gravados com sucesso no arquivo '{nome_arquivo}'!")

except Exception as e:
    print(f"❌ Ocorreu um erro ao escrever o arquivo: {e}")