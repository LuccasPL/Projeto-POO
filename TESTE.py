import tkinter as tk
from tkinter import messagebox

def registrar_trabalhador():
    nome = entry_nome.get()
    idade = entry_idade.get()
    cargo = entry_cargo.get()
    departamento = entry_departamento.get()
    horas_extras = entry_horas_extras.get()
    baixa_medica = entry_baixa_medica.get()
    horas_trabalhadas = entry_horas_trabalhadas.get()

    if nome and idade and cargo and departamento and horas_extras and baixa_medica and horas_trabalhadas:
        with open("trabalhadores.txt", "a") as arquivo:
            arquivo.write(f"Nome: {nome}, Idade: {idade}, Cargo: {cargo}, "
                          f"Departamento: {departamento}, Horas Extras: {horas_extras}, "
                          f"Baixa Médica: {baixa_medica}, Horas Trabalhadas: {horas_trabalhadas}\n")
        messagebox.showinfo("Sucesso", "Dados do trabalhador registrados com sucesso!")
    else:
        messagebox.showwarning("Erro", "Por favor, preencha todos os campos!")

app = tk.Tk()
app.title("Registro de Trabalhadores")

# Nome
label_nome = tk.Label(app, text="Nome:")
label_nome.grid(row=0, column=0)
entry_nome = tk.Entry(app)
entry_nome.grid(row=0, column=1)

# Idade
label_idade = tk.Label(app, text="Idade:")
label_idade.grid(row=1, column=0)
entry_idade = tk.Entry(app)
entry_idade.grid(row=1, column=1)

# Cargo
label_cargo = tk.Label(app, text="Cargo:")
label_cargo.grid(row=2, column=0)
entry_cargo = tk.Entry(app)
entry_cargo.grid(row=2, column=1)

# Departamento
label_departamento = tk.Label(app, text="Departamento:")
label_departamento.grid(row=3, column=0)
entry_departamento = tk.Entry(app)
entry_departamento.grid(row=3, column=1)

# Horas Extras
label_horas_extras = tk.Label(app, text="Horas Extras:")
label_horas_extras.grid(row=4, column=0)
entry_horas_extras = tk.Entry(app)
entry_horas_extras.grid(row=4, column=1)

# Baixa Médica
label_baixa_medica = tk.Label(app, text="Baixa Médica:")
label_baixa_medica.grid(row=5, column=0)
entry_baixa_medica = tk.Entry(app)
entry_baixa_medica.grid(row=5, column=1)

# Horas Trabalhadas
label_horas_trabalhadas = tk.Label(app, text="Horas Trabalhadas:")
label_horas_trabalhadas.grid(row=6, column=0)
entry_horas_trabalhadas = tk.Entry(app)
entry_horas_trabalhadas.grid(row=6, column=1)

# Botão
botao_registrar = tk.Button(app, text="Registrar", command=registrar_trabalhador)
botao_registrar.grid(row=7, column=0, columnspan=2)

app.mainloop()
