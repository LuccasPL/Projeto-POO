import tkinter as tk
from tkinter import ttk
import Conectar_base_de_dados as db


# mostrar o funcionário quando o botão for clicado
def mostrar_funcionario(id_trabalhador):
    print(id_trabalhador.get())
    funcionario = db.trabalhador_por_id(id_trabalhador.get())
    linha = 1
    for info in funcionario:
        ttk.Label(frm, text=info).grid(row = linha, column=1)
        linha += 1
    linha = 3
    # ttk.Label(frm, text=funcionario [0]).grid(row=3, column=0)
    # ttk.Label(frm, text=funcionario [1]).grid(row=4, column=0)
    #label_funcionario.pack()

# Criar a janela
root = tk.Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

# Adicionar um campo de entrada e um botão que busca o funcionário apos o clique
id_trabalhador = tk.StringVar()
ttk.Entry(frm, textvariable=id_trabalhador).grid(row=0, column=0)
ttk.Button(frm, text="Buscar", command=lambda: mostrar_funcionario(id_trabalhador)).grid(row=0, column=1)

# Adicionar um label que mostra o funcionário
label_funcionario = ttk.Label(frm, text="Funcionário ID:")
label_funcionario.grid(row=1, column=0)

label_nome = ttk.Label(frm, text="Nome:")
label_nome.grid(row=2, column=0)

#mostrar a senha em asteriscos
label_senha = ttk.Label(frm, text="Senha:")
label_senha.grid(row=3, column=0)


label = ttk.Label(frm, text="NIF:")
label.grid(row=4, column=0)

label = ttk.Label(frm, text="NIS:")
label.grid(row=5, column=0)

label = ttk.Label(frm, text="E-mail:")
label.grid(row=6, column=0)

label = ttk.Label(frm, text="Estado Civil:")
label.grid(row=7, column=0)

label = ttk.Label(frm, text="Número de Dependentes:")
label.grid(row=8, column=0)

label = ttk.Label(frm, text="Departamento:")
label.grid(row=9, column=0)

label = ttk.Label(frm, text="Cargo:")
label.grid(row=10, column=0)

label = ttk.Label(frm, text="Valor da Hora:")
label.grid(row=11, column=0)

label = ttk.Label(frm, text="Horas Trabalhadas:")
label.grid(row=12, column=0)

label = ttk.Label(frm, text="Valor da Hora Extra:")
label.grid(row=13, column=0)

label = ttk.Label(frm, text="Horas Extras:")
label.grid(row=14, column=0)

label = ttk.Label(frm, text="Baixa Médica:")
label.grid(row=15, column=0)

label = ttk.Label(frm, text="Início do Contrato:")
label.grid(row=16, column=0)

label = ttk.Label(frm, text="Morada:")
label.grid(row=17, column=0)

# Adicionar outro campo de entrada e um botão que busca o funcionário apos o clique
id_trabalhador = tk.StringVar()
ttk.Entry(frm, textvariable=id_trabalhador).grid(row=0, column=0)
ttk.Button(frm, text="Buscar", command=lambda: mostrar_funcionario(id_trabalhador)).grid(row=0, column=1)

# Iniciar o loop da interface
root.mainloop()


