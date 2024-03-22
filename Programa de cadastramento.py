class Produto:
    def __init__(self, nome, descricao, valor, disponivel):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor
        self.disponivel = disponivel

# Função para cadastrar um novo produto
def cadastrar_produto():
    nome = input("Nome do produto: ")
    descricao = input("Descrição do produto: ")
    valor = float(input("Valor do produto: "))
    disponivel = input("Disponível para venda (sim/não): ").lower() == 'sim'
    return Produto(nome, descricao, valor, disponivel)

# Função para exibir a listagem de produtos
def exibir_listagem(produtos):
    print("\nListagem de Produtos:")
    print("{:<30} {:<10}".format("Nome", "Valor"))
    produtos_ordenados = sorted(produtos, key=lambda x: x.valor)
    for produto in produtos_ordenados:
        print("{:<30} {:<10.2f}".format(produto.nome, produto.valor))


# Lista para armazenar os produtos
produtos = []

# Menu principal do programa
while True:
    print("\nMENU:")
    print("1. Cadastrar novo produto")
    print("2. Exibir listagem de produtos")
    print("3. Sair")
    print("-"*25)

    opcao = input("Escolha a opção desejada: ")

    if opcao == '1':
        novo_produto = cadastrar_produto()
        produtos.append(novo_produto)
        exibir_listagem(produtos)
    elif opcao == '2':
        exibir_listagem(produtos)
    elif opcao == '3':
        print("Saindo...")
        break
    else:
        print("Opção inválida!")
