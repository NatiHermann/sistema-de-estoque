#Discente: Natália Hetkowski Hermann

# Lista pra armazenar os produtos 
estoque = []

# Função pra cadastro do produto

def cadastrar_produto():
    print("\n --- Cadastro de Produto ---")

    codigo = input("Digite o código do produto: ")
    for produto in estoque:
        if produto["codigo"] == codigo:
            print("Erro: Já existe um produto com esse código.")
            return
    nome = input("Digite o nome do produto: ")
        