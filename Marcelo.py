import tkinter as tk

class reg_trabalhador:

    def __init__(self, app, row, column, editar=False, text=None):
        if text:
            self.label = tk.Label(app, text=f'{text}:')
            self.label.grid(row=row, column=column)
            self.entry = tk.Entry(app)
            self.entry.grid(row=row, column=column + 1)
            if editar:
                self.edit = tk.Button(app, text="Editar")
                self.edit.grid(row=row, column=column + 2)
            else:
                self.edit = ""

    def get_new_registration(self):
        self.entry.get()


app = tk.Tk()
app.title("Registro de Trabalhadores")

reg_fields = [
    {"f_label": "Nome", "row": 0, "column": 0, "edit": True},
    {"f_label": "Cargo", "row": 2, "column": 0, "edit": True},
    {"f_label": "Departamento", "row": 3, "column": 0, "edit": True},
    {"f_label": "Estado Civil", "row": 4, "column": 0, "edit": True},
    {"f_label": "Número de Dependentes", "row": 5, "column": 0, "edit": True},
    {"f_label": "Início do Contrato", "row": 6, "column": 0, "edit": False},
    {"f_label": "Valor da Hora", "row": 7, "column": 0, "edit": True},
    {"f_label": "Valor da Hora Extra", "row": 8, "column": 0, "edit": True},
    {"f_label": "Horas Trabalhadas", "row": 9, "column": 0, "edit": True},
    {"f_label": "Horas Extras", "row": 10, "column": 0, "edit": True},
    {"f_label": "Dias Trabalhados", "row": 11, "column": 0, "edit": True},
    {"f_label": "Baixa Médica", "row": 12, "column": 0, "edit": True},
    {"f_label": "Morada", "row": 13, "column": 0, "edit": True},
    {"f_label": "Turno", "row": 14, "column": 0, "edit": True},
    {"f_label": "Observações", "row": 15, "column": 0, "edit": True},
]

for field in reg_fields:
    new_func = reg_trabalhador(app, field['row'], field['column'], field['edit'], field['f_label'])

reg_button = tk.Button(app, text="Registrar", command = new_func.get_new_registration())
reg_button.grid(row=16, column=0, columnspan=2)

app.mainloop()