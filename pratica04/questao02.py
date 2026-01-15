#2 - Criar um código que registre as notas de alunos e calcular a média da turma.

def registrar_notas():
    print("=== Registro de Notas da Turma ===")
    
    qtd_alunos = int(input("Digite o número de alunos: "))
    
    notas = []

    for i in range(qtd_alunos):
        nota = float(input(f"Digite a nota do aluno {i+1}: "))
        notas.append(nota)
    
    media = sum(notas) / len(notas)
    
    print("\nNotas registradas:", notas)
    print(f"Média da turma: {media:.2f}")

registrar_notas()