produto = []
quantidade = []
preço = []

concluir = False

while (not concluir):
    print("Digite o nome do produto")
    nomeProduto = input()
    print("Digite a quantidade desse produto ")
    quantidadeProduto = int(input())
    print("Digite o preço do produto")
    preçoProduto = float(input())

    produto.append(nomeProduto)
    quantidade.append(quantidadeProduto)
    preço.append(preçoProduto)

    print("deseja inserir outro item? (s/n)")
    concluir = input () == "n"

    print("seguem abaixo a lista de produtos:")

for i in range(len(produto)):
        print(f"[produtos{i}] : [quantidade{i}] : R$[preço{i}]")

input("pressione Enter para prosseguir")

import os

filename = "minhalista.txt"
file = open(filename, 'w')
for i in range(len(produto)):
      linhaDoArquivo = f"{produto[i]} : {quantidade[i]} : {preço[i]}\n"
      file.write(linhaDoArquivo)
file.close() 

os.system(f"notepad {filename}")