"""2 - Crie um programa que leia um arquivo CSV informado pelo usuário, percorrendo cada linha do arquivo e a exibe na tela, caso o arquivo não seja encontrado, mostre uma mensagem de erro."""

import csv

try:
    # Solicita o nome do arquivo
    nome_arquivo = input("Digite o nome do arquivo CSV para leitura: ")

    # Abre o arquivo para leitura
    with open(nome_arquivo, mode="r", encoding="utf-8") as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            print(linha)  # Cada linha é uma lista

except FileNotFoundError:
    print("❌ Arquivo não encontrado. Verifique o nome e tente novamente.")
except Exception as e:
    print(f"❌ Ocorreu um erro ao ler o arquivo: {e}")