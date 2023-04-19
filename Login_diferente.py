import tkinter as tk
from tkinter import messagebox

usuarios = {
    "admin": {"senha": "admin123", "funcao": "administrador"},
    "gerente": {"senha": "gerente123", "funcao": "gerente"},
}

log_atividades = []

def autenticar_usuario(username, senha):
    if username in usuarios and usuarios[username]["senha"] == senha:
        return usuarios[username]["funcao"]
    else:
        return None

def adicionar_informacao():
    informacao = entry_informacao.get()
    if funcao_usuario != "gerente":
        messagebox.showwarning("Acesso negado!", "Você não tem permissão para adicionar informações.")
        return

    funcionario["informacoes"].append(informacao)
    log_atividades.append({
        "acao": "adicionar_informacao",
        "funcionario": funcionario["nome"],
        "data_hora": datetime.datetime.now().isoformat(),
    })
    messagebox.showinfo("Sucesso", "Informação adicionada com sucesso!")

def ver_atividades():
    atividades = "\n".join([f"{atividade['data_hora']} - {atividade['acao']} - Funcionário: {atividade['funcionario']}" for atividade in log_atividades])
    messagebox.showinfo("Atividades registradas", atividades if atividades else "Nenhuma atividade registrada.")

def login():
    global funcao_usuario
    username = entry_username.get()
    senha = entry_senha.get()

    funcao_usuario = autenticar_usuario(username, senha)
    if not funcao_usuario:
        messagebox.showwarning("Erro", "Usuário ou senha incorretos!")
    else:
        app_login.destroy()

app_login = tk.Tk()
app_login.title("Login")

label_username = tk.Label(app_login, text="Usuário:")
label_username.pack()
entry_username = tk.Entry(app_login)
entry_username.pack()

label_senha = tk.Label(app_login, text="Senha:")
label_senha.pack()
entry_senha = tk.Entry(app_login, show="*")
entry_senha.pack()

button_login = tk.Button(app_login, text="Entrar", command=login)
button_login.pack()

app_login.mainloop()

funcionario = {
    "nome": "João",
    "departamento": "TI",
    "informacoes": [],
}

app = tk.Tk()
app.title("Gerenciamento de Funcionários")

label_informacao = tk.Label(app, text="Adicionar informação:")
label_informacao.grid(row=0, column=0)
entry_informacao = tk.Entry(app)
entry_informacao.grid(row=0, column=1)

button_adicionar = tk.Button(app, text="Adicionar", command=adicionar_informacao)
button_adicionar.grid(row=1, column=0, columnspan=2)

button_ver_atividades = tk.Button(app, text="Ver atividades", command=ver_atividades)
button_ver_atividades.grid(row=2, column=0, columnspan=2)

app.mainloop()
