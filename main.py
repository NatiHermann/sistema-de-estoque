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

# Preço

try:
    preco = float(input("Digite o preço do produto: "))
    if preco < 0:
        print("Erro: o preço não pode ser negativo.")
        return
except ValueError:
    print("Erro: Digite um valor numérico válido para o preço.")
    return

#validação de quantidade
try:
    quantidade = int(input("Digite a quantidade do produto: "))
    if quantidade < 0:
        print("Erro: A quantidade não pode ser negativa.")
        return
except ValueError:
    print("Erro: Digite um número inteiro válido para a quantidade.")
    return

#dicionário

produto = {
    "codigo": codigo,
    "nome": nome,
    "preco": preco,
    "quantidade": quantidade
}

estoque.append(produto)
print("Produto cadastrado com sucesso!")

#Função pro estoque

def calcularTotalProdutos():
    total = 0
    for produto in estoque:
        total+= produto["quantidade"]
    print(f"\nTotal de produtos em estoque: {total}")
    