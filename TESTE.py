import tkinter as tk


def registrar_trabalhador():
    nome = entry_nome.get()
    cargo = entry_cargo.get()
    departamento = entry_departamento.get()
    estado_civil = entry_estado_civil.get()
    num_dependentes = entry_num_dependentes.get()
    inicio_contrato = entry_inicio_contrato.get()
    valor_hora = entry_valor_hora.get()
    valor_hora_extra = entry_valor_hora_extra.get()
    horas_trabalhadas = entry_horas_trabalhadas.get()
    horas_extras = entry_horas_extras.get()
    dias_trabalhados = entry_dias_trabalhados.get()
    baixa_medica = entry_baixa_medica.get()
    morada = entry_morada.get()
    turno = entry_turno.get()
    observacoes = entry_observacoes.get()


app = tk.Tk()
app.title("Registro de Trabalhadores")

# Nome
label_nome = tk.Label(app, text="Nome:")
label_nome.grid(row=0, column=0)
entry_nome = tk.Entry(app)
entry_nome.grid(row=0, column=1)
editar_nome = tk.Button(app, text="Editar")
editar_nome.grid(row=0, column=2)

# Cargo
label_cargo = tk.Label(app, text="Cargo:")
label_cargo.grid(row=2, column=0)
entry_cargo = tk.Entry(app)
entry_cargo.grid(row=2, column=1)
editar_cargo = tk.Button(app, text="Editar")
editar_cargo.grid(row=2, column=2)

# Departamento
label_departamento = tk.Label(app, text="Departamento:")
label_departamento.grid(row=3, column=0)
entry_departamento = tk.Entry(app)
entry_departamento.grid(row=3, column=1)
editar_departamento = tk.Button(app, text="Editar")
editar_departamento.grid(row=3, column=2)

# Estado Civil
label_estado_civil = tk.Label(app, text="Estado Civil:")
label_estado_civil.grid(row=4, column=0)
entry_estado_civil = tk.Entry(app)
entry_estado_civil.grid(row=4, column=1)
editar_estado_civil = tk.Button(app, text="Editar")
editar_estado_civil.grid(row=4, column=2)

# Número de Dependentes
label_num_dependentes = tk.Label(app, text="Número de Dependentes:")
label_num_dependentes.grid(row=5, column=0)
entry_num_dependentes = tk.Entry(app)
entry_num_dependentes.grid(row=5, column=1)
editar_num_dependentes = tk.Button(app, text="Editar")
editar_num_dependentes.grid(row=5, column=2)

# Início do Contrato
label_inicio_contrato = tk.Label(app, text="Início do Contrato:")
label_inicio_contrato.grid(row=6, column=0)
entry_inicio_contrato = tk.Entry(app)
entry_inicio_contrato.grid(row=6, column=1)

# Valor da Hora
label_valor_hora = tk.Label(app, text="Valor da Hora:")
label_valor_hora.grid(row=7, column=0)
entry_valor_hora = tk.Entry(app)
entry_valor_hora.grid(row=7, column=1)
editar_valor_hora = tk.Button(app, text="Editar")
editar_valor_hora.grid(row=7, column=2)

# Valor da Hora Extra
label_valor_hora_extra = tk.Label(app, text="Valor da Hora Extra:")
label_valor_hora_extra.grid(row=8, column=0)
entry_valor_hora_extra = tk.Entry(app)
entry_valor_hora_extra.grid(row=8, column=1)
editar_valor_hora_extra = tk.Button(app, text="Editar")
editar_valor_hora_extra.grid(row=8, column=2)

# Horas Trabalhadas
label_horas_trabalhadas = tk.Label(app, text="Horas Trabalhadas:")
label_horas_trabalhadas.grid(row=9, column=0)
entry_horas_trabalhadas = tk.Entry(app)
entry_horas_trabalhadas.grid(row=9, column=1)
editar_horas_trabalhadas = tk.Button(app, text="Editar")
editar_horas_trabalhadas.grid(row=9, column=2)

# Horas Extras
label_horas_extras = tk.Label(app, text="Horas Extras:")
label_horas_extras.grid(row=10, column=0)
entry_horas_extras = tk.Entry(app)
entry_horas_extras.grid(row=10, column=1)
editar_horas_extras = tk.Button(app, text="Editar")
editar_horas_extras.grid(row=10, column=2)

# Dias Trabalhados
label_dias_trabalhados = tk.Label(app, text="Dias Trabalhados:")
label_dias_trabalhados.grid(row=11, column=0)
entry_dias_trabalhados = tk.Entry(app)
entry_dias_trabalhados.grid(row=11, column=1)
editar_dias_trabalhados = tk.Button(app, text="Editar")
editar_dias_trabalhados.grid(row=11, column=2)

# Baixa Médica
label_baixa_medica = tk.Label(app, text="Baixa Médica:")
label_baixa_medica.grid(row=12, column=0)
entry_baixa_medica = tk.Entry(app)
entry_baixa_medica.grid(row=12, column=1)
editar_baixa_medica = tk.Button(app, text="Editar")
editar_baixa_medica.grid(row=12, column=2)

# Morada
label_morada = tk.Label(app, text="Morada:")
label_morada.grid(row=13, column=0)
entry_morada = tk.Entry(app)
entry_morada.grid(row=13, column=1)
editar_morada = tk.Button(app, text="Editar")
editar_morada.grid(row=13, column=2)

# Turno
label_turno = tk.Label(app, text="Turno:")
label_turno.grid(row=14, column=0)
entry_turno = tk.Entry(app)
entry_turno.grid(row=14, column=1)
editar_turno = tk.Button(app, text="Editar")
editar_turno.grid(row=14, column=2)

# Observações
label_observacoes = tk.Label(app, text="Observações:")
label_observacoes.grid(row=15, column=0)
entry_observacoes = tk.Entry(app)
entry_observacoes.grid(row=15, column=1)
editar_observacoes = tk.Button(app, text="Editar")
editar_observacoes.grid(row=15, column=2)

# Botão
botao_registrar = tk.Button(app, text="Registrar", command=registrar_trabalhador)
botao_registrar.grid(row=16, column=0, columnspan=2)

app.mainloop()
