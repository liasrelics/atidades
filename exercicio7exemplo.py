alunos = []
notas = []

concluir = False

while (not concluir):
    print("digite o nome do aluno:")
    nomeAluno = input()
    print("digite a nota do aluno")
    notaAluno = int(input())

    if(notaAluno < 5): print("misericordia")
    elif(notaAluno < 7): print("tá quase")
    else: print("passouuuuuuu")

    alunos.append(nomeAluno)
    notas.append(notaAluno)

    print("deseja inserir outra nota? (s/n)")
    concluir = input () == "n"

    print("seguem abaixo tdas as notas digitadas:")
    print("aluno : nota")
for i in range(len(alunos)):
    print(f"{alunos[i]} : {notas[i]}")


input("pressione Enter para terminar...")