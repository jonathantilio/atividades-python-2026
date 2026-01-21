"""3 - Crie um programa que leia e escreva arquivos no formato JSON, que salve em um dicionário com nome, idade e cidade em um arquivo JSON e depois leia o mesmo arquivo exibindo os dados, caso o arquivo não existir ou ocorrer erro ao salvar, mostre uma mensagem de falha. """

import json

# Dicionário com dados fictícios
pessoa = {
    "nome": "João",
    "idade": 28,
    "cidade": "Curitiba"
}

try:
    # Solicita o nome do arquivo
    nome_arquivo = input("Digite o nome do arquivo JSON: ")

    # Salva os dados no arquivo
    with open(nome_arquivo, mode="w", encoding="utf-8") as arquivo:
        json.dump(pessoa, arquivo, ensure_ascii=False, indent=4)

    print(f"✅ Dados salvos com sucesso no arquivo '{nome_arquivo}'!")

    # Lê os dados do mesmo arquivo
    with open(nome_arquivo, mode="r", encoding="utf-8") as arquivo:
        dados_carregados = json.load(arquivo)
        print("📖 Conteúdo do arquivo JSON:")
        print(dados_carregados)

except FileNotFoundError:
    print("❌ Arquivo não encontrado.")
except Exception as e:
    print(f"❌ Ocorreu um erro: {e}")