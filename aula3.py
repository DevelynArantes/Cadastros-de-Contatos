contatos = []

def adicionar_contato(nome, telefone):
    contatos.append({"nome": nome, "telefone": telefone})
    print(f"Contato {nome} adicionado com sucesso!")

def listar_contatos():
    if contatos:
        print("Lista de contatos:")
        for i, contato in enumerate(contatos, start=1):
            print(f"{i}. {contato['nome']} - {contato['telefone']}")
    else:
        print("Nenhum contato cadastrado.")

def buscar_contato(nome):
    for contato in contatos:
        if contato["nome"].lower() == nome.lower():
            print(f"Contato encontrado: {contato['nome']} - {contato['telefone']}")
            return
    print("Contato não encontrado.")

def menu():
    while True:
        print("\nMenu:")
        print("1 - Adicionar contato")
        print("2 - Listar contatos")
        print("3 - Buscar contato")
        print("4 - Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Nome do contato: ")
            telefone = input("Telefone do contato: ")
            adicionar_contato(nome, telefone)
        elif escolha == "2":
            listar_contatos()
        elif escolha == "3":
            nome = input("Digite o nome para buscar: ")
            buscar_contato(nome)
        elif escolha == "4":
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Rodando o programa
menu()

    









    







    
     


  

    








                  

    











        


         

        


    

