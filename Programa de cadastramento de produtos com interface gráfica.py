import tkinter as tk
from tkinter import messagebox

# Classe Produto
class Produto:
    def __init__(self, nome, descricao, valor, disponivel):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor
        self.disponivel = disponivel
        
# Função para cadastrar um novo produto
def cadastrar_produto():
    nome = entry_nome.get()
    descricao = entry_descricao.get()
    valor = float(entry_valor.get())
    disponivel = var_disponivel.get() == 1 
    if nome and descricao and valor:
        produto = Produto(nome, descricao, valor, disponivel)
        produtos.append(produto)
        exibir_listagem()
        limpar_campos()
        messagebox.showinfo("Sucesso", "Produto cadastrado com sucesso!")
    else:
        messagebox.showwarning("Atenção", "Preencha todos os campos corretamente.")
        
# Função para exibir a listagem de produtos
def exibir_listagem():
    listbox_produtos.delete(0, tk.END)  # Limpar a listagem anterior
    produtos_ordenados = sorted(produtos, key=lambda x: x.valor)
    for produto in produtos_ordenados:
        listbox_produtos.insert(tk.END, f"{produto.nome} - R$ {produto.valor:.2f}")

# Função para limpar os campos do formulário
def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_descricao.delete(0, tk.END)
    entry_valor.delete(0, tk.END)

    var_disponivel.set(0)
# Lista para armazenar os produtos
produtos = []

# Configuração da janela principal
janela = tk.Tk()
janela.title("Cadastro de Produtos")

# Labels e campos de entrada
label_nome = tk.Label(janela, text="Nome:")
label_nome.grid(row=0, column=0, padx=10, pady=5)
entry_nome = tk.Entry(janela)
entry_nome.grid(row=0, column=1, padx=10, pady=5)
label_descricao = tk.Label(janela, text="Descrição:")
label_descricao.grid(row=1, column=0, padx=10, pady=5)
entry_descricao = tk.Entry(janela)
entry_descricao.grid(row=1, column=1, padx=10, pady=5)
label_valor = tk.Label(janela, text="Valor:")
label_valor.grid(row=2, column=0, padx=10, pady=5)
entry_valor = tk.Entry(janela)
entry_valor.grid(row=2, column=1, padx=10, pady=5)
var_disponivel = tk.IntVar()
check_disponivel = tk.Checkbutton(janela, text="Disponível para venda", variable=var_disponivel)
check_disponivel.grid(row=3, column=1, padx=10, pady=5)

# Botão para cadastrar produto
botao_cadastrar = tk.Button(janela, text="Cadastrar Produto", command=cadastrar_produto)
botao_cadastrar.grid(row=4, column=1, padx=10, pady=5)

# Listbox para exibir os produtos
listbox_produtos = tk.Listbox(janela, width=50, height=10)
listbox_produtos.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

# Rodar a janela principal
janela.mainloop()
