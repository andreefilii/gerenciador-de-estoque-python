import json


produtos = {
    "melancia":{
        "quantidade" : 4,
        "preço" : 7.90
    },
    "arroz" : {
        "quantidade" : 5,
        "preço" : 6.89
    },
    "feijão":{
       "quantidade": 0,
       "preço" : 5.49
    }

    }


# Adicionar produto

# Listar produtos

# Remover produto

# Atualizar quantidade de produto

# Sair




def adicionar_produtos(produtos , nome_produto , quantidade , preco):
    produtos[nome_produto] = {
        "quantidade" : quantidade,
        "preço" : preco
    }
    return f"Produto ({nome_produto}), foi adicionado com sucesso com o preço R${preco}, Quantidade: {quantidade}"
     
def remover_produtos(produtos, nome_produto):
    del produtos[nome_produto]
    return f"{nome_produto}, Removido com sucesso do estoque!!"


def listar_produtos(produtos):
 disponivel = {}
 indisponivel = {}
 for produto , dados in produtos.items():
    if dados["quantidade"] == 0 :
       indisponivel[produto] = dados
    else:
       disponivel[produto] = dados
 for produto , dados in sorted (disponivel.items(),
    key = lambda item : item[0]):
    print( f""""
        Nome: {produto}
        Quantidade: {dados["quantidade"]} Disponvel✔️​
        Preço : {dados["preço"]}
    """
    )
 for produto , dados in sorted (indisponivel.items(),
    key = lambda item : item[0]):
    print(f"""
        Nome: {produto}
        Quantidade: {dados["quantidade"]}​ Indisponivel❌​
        Preço : {dados["preço"]}

""")


def atualizar_quantidade(produtos , nome_produto, quantidade):
 produtos[nome_produto]["quantidade"] = quantidade
 return f"""Quantidade atualizada com sucesso
    Nome: {nome_produto} Quatidade: {quantidade}"""


def carregar_estoque():
    try:
        with open ("estoque.json", "r") as estoque:
            return json.load(estoque)
    except FileNotFoundError :
       return {}
    
def salvar_estoque(produtos):
      with open ("estoque.json" , "w") as estoque:
                json.dump(produtos,estoque)


def buscar_produto(produtos , nome_produto):
    if nome_produto not in produtos:
        return "Produto não está no estoque"
    dados = produtos[nome_produto]
    if dados["quantidade"] == 0 :
        return f""""
        Nome: {nome_produto}
        Quantidade : {dados["quantidade"]} Indisponivel❌
        Preço: {dados["preço"]}
        """
    else:
        return f""""
        Nome: {nome_produto}
        Quantidade : {dados["quantidade"]} Disponvel✔️​
        Preço: {dados["preço"]}
        """



def menu():
    print("""
            ----MENU----
          1: Adicionar produto

          2: Listar produtos

          3: Remover produto

          4: Atualizar quantidade de produto

          5: Buscar Produto

          6: Sair
          ---------------------
""")



def main(produtos):
   
 
    while True:
        menu()
        opcao = input("Escolha uma opção\n")
        if opcao == "1":
            try:
                nome_produto = str(input("Digite o nome do Produto\n")).lower()
                if nome_produto in produtos:
                    print(f"{nome_produto} , ja existe no estoque")
                else:
                    quantidade = int(input(f"Digite a quantidade do produto ({nome_produto})\n"))
                    preco = float(input("Qual o preço do produto?\n"))
                    print(adicionar_produtos(produtos , nome_produto, quantidade , preco  ) )
                    salvar_estoque(produtos)

            except ValueError as erro:
                print("Digite uma quantidade valida")
            except TypeError as erro:
                print("Digite um Nome Valido")
            
        elif opcao == "2":
                if produtos == {}:
                        print("Nao Há nenhum produto no estoque")
                else:
                    listar_produtos(produtos) 

        elif opcao == "3":
            try:
                nome_produto = str(input("Qual o nome do produto que deseja remover?\n")).lower()
                if nome_produto not in produtos:
                        print("Esse produto não existe no estoque")
                else:   
                        print(remover_produtos(produtos, nome_produto))
                        salvar_estoque(produtos)
            except TypeError as erro:
                print("Digite um Nome Valido")

        elif opcao == "4":
            try:
                nome_produto = str(input("Nome Do Produto\n")).lower()
                if nome_produto not in produtos:
                    print("Produto não encotrado ou não existi no estoque""")
                else:
                    quantidade = int(input(f"Digite á quantidade do produto ({nome_produto})\n"))
                    print(atualizar_quantidade(produtos , nome_produto, quantidade))
                    salvar_estoque(produtos)
            except ValueError as erro:
                print("Digite uma quantidade valida")
            except TypeError as erro:
                print("Digite um Nome Valido")
            
        elif opcao == "5":
            try:
                nome_produto = str(input("Qual nome do produo deseja buscar?\n")).lower()
                print(buscar_produto(produtos , nome_produto))   
            except TypeError as erro:
                print("Digite um Nome Valido")

        elif opcao == "6":
            print("SAINDO......")
            salvar_estoque(produtos)
            break
        else:
            print("Escolha uma opção valida!!")
produtos = carregar_estoque()
main(produtos)                   


