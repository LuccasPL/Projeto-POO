import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
# Função para autenticar o gerente
def autenticar():
    usuario = usuario_entry.get()
    senha = senha_entry.get()

    # Aqui você pode verificar o nome de usuário e a senha com o banco de dados ou arquivo
    if usuario == "gerente" and senha == "1234":
        messagebox.showinfo("Sucesso", "Autenticação bem-sucedida!")
        janela_login.destroy()
        janela_informacoes_funcionarios()
    else:
        messagebox.showerror("Erro", "Nome de usuário ou senha incorretos!")


def janela_informacoes_funcionarios():
    janela_funcionarios = tk.Tk()
    janela_funcionarios.title("Informações dos Funcionários")

    # Criação da tabela
    colunas = ("ID", "Nome", "Cargo", "Departamento", "Salário")
    tabela_funcionarios = ttk.Treeview(janela_funcionarios, columns=colunas, show="headings")

    # Configurar colunas
    for coluna in colunas:
        tabela_funcionarios.heading(coluna, text=coluna)
        tabela_funcionarios.column(coluna, anchor="center", width=100)

    # Exemplo de dados dos funcionários que podem ser obtidos de um banco de dados
    funcionarios = [
        (1, "João", "Analista", "TI", 5000),
        (2, "Maria", "Gerente", "RH", 6000),
        (3, "Pedro", "Engenheiro", "Produção", 7000),
        (4, "Ana", "Assistente", "Administração", 3000),
    ]

    # Inserir dados dos funcionários na tabela
    for funcionario in funcionarios:
        tabela_funcionarios.insert("", "end", values=funcionario)

    tabela_funcionarios.pack(fill="both", expand=True, padx=10, pady=10)
    janela_funcionarios.mainloop()


# Criação da janela de login
janela_login = tk.Tk()
janela_login.title("Login do Gerente")

# Widgets para nome de usuário e senha
usuario_label = tk.Label(janela_login, text="Nome de usuário:")
usuario_label.grid(row=0, column=0, padx=10, pady=10)

usuario_entry = tk.Entry(janela_login)
usuario_entry.grid(row=0, column=1, padx=10, pady=10)

senha_label = tk.Label(janela_login, text="Senha:")
senha_label.grid(row=1, column=0, padx=10, pady=10)

senha_entry = tk.Entry(janela_login, show="*")
senha_entry.grid(row=1, column=1, padx=10, pady=10)

# Botão de login
botao_login = tk.Button(janela_login, text="Login", command=autenticar)
botao_login.grid(row=2, columnspan=2, pady=10)

janela_login.mainloop()
