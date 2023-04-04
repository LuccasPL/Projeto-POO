import tkinter as tk
from tkinter import messagebox

def verificar_login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    if usuario == "admin" and senha == "123":
        messagebox.showinfo("Login", "Acesso concedido!")
        app.destroy()  # Fecha a janela de login
        criar_tela_cadastro()  # Abre a tela de cadastro
    else:
        messagebox.showerror("Login", "Usuário e/ou senha incorretos.")

def criar_tela_cadastro():
    def cadastrar_funcionario():
        nome = entry_nome.get()
        cargo = entry_cargo.get()
        salario = entry_salario.get()

        # Adicione a lógica para salvar os dados do funcionário aqui, como salvar em um banco de dados ou arquivo.
        messagebox.showinfo("Cadastro", f"Funcionário {nome} cadastrado com sucesso!")

    cadastro_app = tk.Tk()
    cadastro_app.title("Cadastro de Funcionários")

    frame_cadastro = tk.Frame(cadastro_app)
    frame_cadastro.pack(pady=10)

    label_nome = tk.Label(frame_cadastro, text="Nome:")
    label_nome.grid(row=0, column=0, sticky="w")

    entry_nome = tk.Entry(frame_cadastro)
    entry_nome.grid(row=0, column=1)

    label_cargo = tk.Label(frame_cadastro, text="Cargo:")
    label_cargo.grid(row=1, column=0, sticky="w")

    entry_cargo = tk.Entry(frame_cadastro)
    entry_cargo.grid(row=1, column=1)

    label_salario = tk.Label(frame_cadastro, text="Salário:")
    label_salario.grid(row=2, column=0, sticky="w")

    entry_salario = tk.Entry(frame_cadastro)
    entry_salario.grid(row=2, column=1)

    button_cadastrar = tk.Button(frame_cadastro, text="Cadastrar", command=cadastrar_funcionario)
    button_cadastrar.grid(row=3, columnspan=2, pady=10)

    cadastro_app.mainloop()

app = tk.Tk()
app.title("Tela de Login")

frame = tk.Frame(app)
frame.pack(pady=10)

label_usuario = tk.Label(frame, text="Usuário:")
label_usuario.grid(row=0, column=0, sticky="w")

entry_usuario = tk.Entry(frame)
entry_usuario.grid(row=0, column=1)

label_senha = tk.Label(frame, text="Senha:")
label_senha.grid(row=1, column=0, sticky="w")

entry_senha = tk.Entry(frame, show="*")
entry_senha.grid(row=1, column=1)

button_login = tk.Button(frame, text="Login", command=verificar_login)
button_login.grid(row=2, columnspan=2, pady=10)

app.mainloop()
