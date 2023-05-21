import tkinter as tk
from tkinter import ttk
import Conectar_base_de_dados as db

# mostrar o funcionário quando o botão for clicado
def mostrar_funcionario(id_trabalhador):
    print(id_trabalhador.get())
    funcionario = db.trabalhador_por_id(id_trabalhador.get())
    linha = 3
    for info in funcionario:
        ttk.Label(frm, text=info).grid(row = linha, column=0)
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


# Iniciar o loop da interface
root.mainloop()


