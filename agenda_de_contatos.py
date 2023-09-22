#Júlia Vitória e Geovanna Letícia, 2B

# *  Com base no exercicio anterior, crie um programa em python que gerencie uma agenda de contatos, com nome, endereço, 
# * e telefone, e que classifique esses contatos entre, pessoais, profissionais e romanticos...

# ? A Agenda de contatos deverá ser armazenada em arquivo, todas as consultas devem ser feitas diretamente 
# ? no arquivo e todas as alterações devem ser salvas nele!
# ? Esse programa deve conter funções para Criar contato, Editar contato, Excluir Contato e Listar os contatos existentes
# ? Salvar agenda
# ? Fechar agenda
# ? Deve ser possivel fechar a agenda "Sem salvar" e ao Fechar a agenda,  o sistema deve perguntar se o usuário deseja salvar

print("AGENDA DE CONTATO")
print("_____________________")

contatos = []

def criar_contato(nome, endereco, telefone, categoria):
    contato = {
        "Nome": nome,
        "Endereço": endereco,
        "Telefone": telefone,
        "Categoria": categoria
    }
    contatos.append(contato)

def adicionar_contato():
    nome = input("Digite o nome do contato: ")
    endereco = input("Digite o endereço do contato: ")
    telefone = input("Digite o telefone do contato: ")
    categoria = input("Digite a categoria [Pessoal, Profissional, Romântico]: ")
    criar_contato(nome, endereco, telefone, categoria)

def listar_contatos():
    for contato in contatos:
        print("Contato:")
        print(f"Nome: {contato['Nome']}")
        print(f"Endereço: {contato['Endereço']}")
        print(f"Telefone: {contato['Telefone']}")
        print(f"Categoria: {contato['Categoria']}")

def editar_contato():
    nome_a_editar = input("Digite o nome do contato que deseja editar: ")
    for contato in contatos:
        if contato["Nome"] == nome_a_editar:
            novo_nome = input(f"Digite o novo nome para o contato [{contato['Nome']}]: ") or contato['Nome']
            novo_endereco = input(f"Digite o novo endereço para o contato [{contato['Endereço']}]: ") or contato['Endereço']
            novo_telefone = input(f"Digite o novo telefone para o contato [{contato['Telefone']}]: ") or contato['Telefone']
            nova_categoria = input(f"Digite a nova categoria para o contato [{contato['Categoria']}]: ") or contato['Categoria']
            
            contato["Nome"] = novo_nome
            contato["Endereço"] = novo_endereco
            contato["Telefone"] = novo_telefone
            contato["Categoria"] = nova_categoria
            print("Contato editado com sucesso!")
            return
    print(f"Contato com o nome '{nome_a_editar}' não encontrado na agenda")

def excluir_contato():
    nome_para_excluir = input("Digite o nome do contato que deseja excluir: ")
    for contato in contatos:
        if contato["Nome"] == nome_para_excluir:
            contatos.remove(contato)
            print(f"Contato '{nome_para_excluir}' excluído com sucesso!")
            return
    print(f"Contato com o nome '{nome_para_excluir}' não encontrado na agenda")

def salvar_agenda():
    arquivo_agenda = input("Digite o nome do arquivo para salvar a agenda: ")
    with open(arquivo_agenda, 'w') as arquivo:
        for contato in contatos:
            arquivo.write(f"{contato['Nome']}, {contato['Endereço']}, {contato['Telefone']}, {contato['Categoria']}\n")
    print(f"Agenda salva no arquivo '{arquivo_agenda}' com sucesso")

def fechar_agenda():
    opcao_fechar = input("Deseja salvar a agenda antes de fechar? ('S' para salvar, 'ENTER' para fechar sem salvar): ")
    if opcao_fechar.lower() == "s":
        salvar_agenda()

while True:
    print("\nEscolha uma das opções a seguir:")
    print("1. Adicionar contato")
    print("2. Listar contatos")
    print("3. Editar contato")
    print("4. Excluir contato")
    print("5. Salvar agenda")
    print("6. Fechar agenda")

    opcao = input("Digite o número da opção desejada (ou 'q' para sair): ")

    if opcao == "1":
        adicionar_contato()
    elif opcao == "2":
        listar_contatos()
    elif opcao == "3":
        editar_contato()
    elif opcao == "4":
        excluir_contato()
    elif opcao == "5":
        salvar_agenda()
    elif opcao == "6":
        fechar_agenda()
    elif opcao.lower() == "q":
        break
    else:
        print("Opção inválida. Tente novamente.")