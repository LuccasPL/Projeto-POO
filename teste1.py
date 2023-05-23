import tkinter as tk
import mysql.connector
from tkinter import messagebox
from tkinter import ttk


def imposto_ssc(salario):
    if salario <= 1000000:
        return 0.11

# funcao que vai calcular o desconto do salario dependendo do estado civil, numero de dependentes e salario
def desconto(salario, estado_civil, num_dependentes):
    if estado_civil == "S" and num_dependentes <= 1:
        return salario * 0.07
    elif estado_civil == "S" and num_dependentes == 2:
        return salario * 0.06
    elif estado_civil == "S" and num_dependentes == 3:
        return salario * 0.05
    elif estado_civil == "S" and num_dependentes == 4:
        return salario * 0.04
    elif estado_civil == "S" and num_dependentes >= 5:
        return salario * 0.03
    elif estado_civil == "C" and num_dependentes <= 1:
        return salario * 0.06
    elif estado_civil == "C" and num_dependentes == 2:
        return salario * 0.05
    elif estado_civil == "C" and num_dependentes == 3:
        return salario * 0.03
    elif estado_civil == "C" and num_dependentes == 4:
        return salario * 0.01
    elif estado_civil == "C" and num_dependentes >= 5:
        return salario
    elif estado_civil == "V" and num_dependentes <= 1:
        return salario * 0.06
    elif estado_civil == "V" and num_dependentes == 2:
        return salario * 0.05
    elif estado_civil == "V" and num_dependentes == 3:
        return salario * 0.04
    elif estado_civil == "V" and num_dependentes == 4:
        return salario * 0.03
    elif estado_civil == "V" and num_dependentes >= 5:
        return salario * 0.02
    elif estado_civil == "D" and num_dependentes <= 1:
        return salario * 0.05
    elif estado_civil == "D" and num_dependentes == 2:
        return salario * 0.04
    elif estado_civil == "D" and num_dependentes == 3:
        return salario * 0.03
    elif estado_civil == "D" and num_dependentes == 4:
        return salario * 0.02
    elif estado_civil == "D" and num_dependentes >= 5:
        return salario * 0.01

# funcao que vai calcular o salario liquido
def calcular_salario():

    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="78517231Le!",
        database="projeto"
    )
    cursor = db.cursor()


    cursor.execute("SELECT estado_civil, num_dependentes, valor_hora, horas_trabalhadas, valor_hora_extra, horas_extras FROM trabalhador WHERE id_trabalhador=%s", (id_trabalhador_entry.get(),))
    result = cursor.fetchone()

    if result is None:
        salary_label.config(text="Nenhum funcionário encontrado com o ID fornecido")
        return

    estado_civil, num_dependentes, valor_hora, horas_trabalhadas, valor_hora_extra, horas_extras = result


    salario = horas_trabalhadas * valor_hora + horas_extras * valor_hora_extra
    salario1= salario - (salario * imposto_ssc(salario))
    salario2 = salario1 - desconto(salario1, estado_civil, num_dependentes)

# formatar o salario para ter apenas 2 casas decimais
    salario2 = f"{salario2:.2f}"
    salary_label.config(text=f"O salário desse mes do funcionário é de {salario2} €")

def janela_salario():

    salary_window = tk.Toplevel(root)


    global id_trabalhador_entry
    id_trabalhador_label = tk.Label(salary_window, text="ID do Trabalhador:")
    id_trabalhador_label.grid(row=0, column=0)
    id_trabalhador_entry = tk.Entry(salary_window)
    id_trabalhador_entry.grid(row=0, column=1)

    calculate_button = tk.Button(salary_window, text="Calcular Salário", command=calcular_salario)
    calculate_button.grid(row=1, column=1)


    global salary_label
    salary_label = tk.Label(salary_window, text="")
    salary_label.grid(row=2, column=0, columnspan=2)

    nextButton = tk.Button(salary_window, text="Próximo", command=novaJanela)
    nextButton.grid(row=1, column=2)

def novaJanela():

    def insert_employee():
        # Conecte-se ao banco de dados
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="78517231Le!",
            database="projeto"
        )
        cursor = db.cursor()

        # consulta SQL
        sql = """
            INSERT INTO trabalhador 
            SET nome=%s, senha=%s, num_nif=%s, num_niss=%s, email=%s, estado_civil=%s, num_dependentes=%s, departamento=%s, cargo=%s, valor_hora=%s, 
            horas_trabalhadas=%s, valor_hora_extra=%s, horas_extras=%s, num_baixa_medica=%s, inicio_contrato=%s, morada=%s
            """

        # Execute a consulta
        cursor.execute(sql, (
            nome_entry.get(),
            senha_entry.get(),
            nif_entry.get(),
            niss_entry.get(),
            email_entry.get(),
            estado_civil_entry.get(),
            num_dependentes_entry.get(),
            departamento_entry.get(),
            cargo_entry.get(),
            valor_hora_entry.get(),
            horas_trabalhadas_entry.get(),
            valor_hora_extra_entry.get(),
            horas_extras_entry.get(),
            num_baixa_medica_entry.get(),
            inicio_contrato_entry.get(),
            morada_entry.get()
        ))

        db.commit()

        messagebox.showinfo("Informação", "Novo funcionário inserido com sucesso!")


    root = tk.Tk()
    root.title("Inserir dados do funcionário")

    # campos de entrada para cada atributo
    nome_label = tk.Label(root, text="Nome:")
    nome_label.grid(row=0, column=0)
    nome_entry = tk.Entry(root)
    nome_entry.grid(row=0, column=1)

    senha_label = tk.Label(root, text="Senha:")
    senha_label.grid(row=1, column=0)
    senha_entry = tk.Entry(root)
    senha_entry.grid(row=1, column=1)

    nif_label = tk.Label(root, text="NIF:")
    nif_label.grid(row=2, column=0)
    nif_entry = tk.Entry(root)
    nif_entry.grid(row=2, column=1)

    niss_label = tk.Label(root, text="NISS:")
    niss_label.grid(row=3, column=0)
    niss_entry = tk.Entry(root)
    niss_entry.grid(row=3, column=1)

    email_label = tk.Label(root, text="Email:")
    email_label.grid(row=4, column=0)
    email_entry = tk.Entry(root)
    email_entry.grid(row=4, column=1)

    estado_civil_label = tk.Label(root, text="Estado Civil:")
    estado_civil_label.grid(row=5, column=0)
    estado_civil_entry = tk.Entry(root)
    estado_civil_entry.grid(row=5, column=1)

    num_dependentes_label = tk.Label(root, text="Número de dependentes:")
    num_dependentes_label.grid(row=6, column=0)
    num_dependentes_entry = tk.Entry(root)
    num_dependentes_entry.grid(row=6, column=1)

    departamento_label = tk.Label(root, text="Departamento:")
    departamento_label.grid(row=7, column=0)
    departamento_entry = tk.Entry(root)
    departamento_entry.grid(row=7, column=1)

    cargo_label = tk.Label(root, text="Cargo:")
    cargo_label.grid(row=8, column=0)
    cargo_entry = tk.Entry(root)
    cargo_entry.grid(row=8, column=1)

    valor_hora_label = tk.Label(root, text="Valor da hora:")
    valor_hora_label.grid(row=9, column=0)
    valor_hora_entry = tk.Entry(root)
    valor_hora_entry.grid(row=9, column=1)

    horas_trabalhadas_label = tk.Label(root, text="Horas trabalhadas:")
    horas_trabalhadas_label.grid(row=10, column=0)
    horas_trabalhadas_entry = tk.Entry(root)
    horas_trabalhadas_entry.grid(row=10, column=1)

    valor_hora_extra_label = tk.Label(root, text="Valor da hora extra:")
    valor_hora_extra_label.grid(row=11, column=0)
    valor_hora_extra_entry = tk.Entry(root)
    valor_hora_extra_entry.grid(row=11, column=1)

    horas_extras_label = tk.Label(root, text="Horas extras:")
    horas_extras_label.grid(row=12, column=0)
    horas_extras_entry = tk.Entry(root)
    horas_extras_entry.grid(row=12, column=1)

    num_baixa_medica_label = tk.Label(root, text="Número de baixas médicas:")
    num_baixa_medica_label.grid(row=13, column=0)
    num_baixa_medica_entry = tk.Entry(root)
    num_baixa_medica_entry.grid(row=13, column=1)

    inicio_contrato_label = tk.Label(root, text="Início do contrato:")
    inicio_contrato_label.grid(row=14, column=0)
    inicio_contrato_entry = tk.Entry(root)
    inicio_contrato_entry.grid(row=14, column=1)

    morada_label = tk.Label(root, text="Morada:")
    morada_label.grid(row=15, column=0)
    morada_entry = tk.Entry(root)
    morada_entry.grid(row=15, column=1)

    # Crie um botão para atualizar o funcionário
    insert_button = tk.Button(root, text="Inserir Funcionário", command=insert_employee)
    insert_button.grid(row=16, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

def janela_atualizar():
    def update_employee():
        atualizar_funcionario = tk.Toplevel(root)
        # Conecte-se ao banco de dados
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="78517231Le!",
            database="projeto"
        )
        cursor = db.cursor()

        # consulta SQL
        sql = """
        UPDATE trabalhador 
        SET nome=%s, senha=%s, num_nif=%s, num_niss=%s, email=%s, estado_civil=%s, num_dependentes=%s, departamento=%s, cargo=%s, valor_hora=%s, 
        horas_trabalhadas=%s, valor_hora_extra=%s, horas_extras=%s, num_baixa_medica=%s, inicio_contrato=%s, morada=%s
        WHERE id_trabalhador=%s
        """

        # Execute a consulta
        cursor.execute(sql, (
            nome_entry.get(),
            senha_entry.get(),
            nif_entry.get(),
            niss_entry.get(),
            email_entry.get(),
            estado_civil_entry.get(),
            num_dependentes_entry.get(),
            departamento_entry.get(),
            cargo_entry.get(),
            valor_hora_entry.get(),
            horas_trabalhadas_entry.get(),
            valor_hora_extra_entry.get(),
            horas_extras_entry.get(),
            num_baixa_medica_entry.get(),
            inicio_contrato_entry.get(),
            morada_entry.get(),
            id_trabalhador_entry.get()
        ))

        db.commit()

        messagebox.showinfo("Informação", "Dados do funcionário atualizados com sucesso")

    root = tk.Tk()
    root.title("Atualizar dados do funcionário")

    id_trabalhador_label = tk.Label(root, text="ID do funcionário:")
    id_trabalhador_label.grid(row=0, column=0)
    id_trabalhador_entry = tk.Entry(root)
    id_trabalhador_entry.grid(row=0, column=1)

    nome_label = tk.Label(root, text="Nome:")
    nome_label.grid(row=1, column=0)
    nome_entry = tk.Entry(root)
    nome_entry.grid(row=1, column=1)

    senha_label = tk.Label(root, text="Senha:")
    senha_label.grid(row=2, column=0)
    senha_entry = tk.Entry(root)
    senha_entry.grid(row=2, column=1)

    nif_label = tk.Label(root, text="NIF:")
    nif_label.grid(row=3, column=0)
    nif_entry = tk.Entry(root)
    nif_entry.grid(row=3, column=1)

    niss_label = tk.Label(root, text="NISS:")
    niss_label.grid(row=4, column=0)
    niss_entry = tk.Entry(root)
    niss_entry.grid(row=4, column=1)

    email_label = tk.Label(root, text="Email:")
    email_label.grid(row=5, column=0)
    email_entry = tk.Entry(root)
    email_entry.grid(row=5, column=1)

    estado_civil_label = tk.Label(root, text="Estado civil:")
    estado_civil_label.grid(row=6, column=0)
    estado_civil_entry = tk.Entry(root)
    estado_civil_entry.grid(row=6, column=1)

    num_dependentes_label = tk.Label(root, text="Número de dependentes:")
    num_dependentes_label.grid(row=7, column=0)
    num_dependentes_entry = tk.Entry(root)
    num_dependentes_entry.grid(row=7, column=1)

    departamento_label = tk.Label(root, text="Departamento:")
    departamento_label.grid(row=8, column=0)
    departamento_entry = tk.Entry(root)
    departamento_entry.grid(row=8, column=1)

    cargo_label = tk.Label(root, text="Cargo:")
    cargo_label.grid(row=9, column=0)
    cargo_entry = tk.Entry(root)
    cargo_entry.grid(row=9, column=1)

    valor_hora_label = tk.Label(root, text="Valor da hora:")
    valor_hora_label.grid(row=10, column=0)
    valor_hora_entry = tk.Entry(root)
    valor_hora_entry.grid(row=10, column=1)

    horas_trabalhadas_label = tk.Label(root, text="Horas trabalhadas:")
    horas_trabalhadas_label.grid(row=11, column=0)
    horas_trabalhadas_entry = tk.Entry(root)
    horas_trabalhadas_entry.grid(row=11, column=1)

    valor_hora_extra_label = tk.Label(root, text="Valor da hora extra:")
    valor_hora_extra_label.grid(row=12, column=0)
    valor_hora_extra_entry = tk.Entry(root)
    valor_hora_extra_entry.grid(row=12, column=1)

    horas_extras_label = tk.Label(root, text="Horas extras:")
    horas_extras_label.grid(row=13, column=0)
    horas_extras_entry = tk.Entry(root)
    horas_extras_entry.grid(row=13, column=1)

    num_baixa_medica_label = tk.Label(root, text="Número de baixas médicas:")
    num_baixa_medica_label.grid(row=14, column=0)
    num_baixa_medica_entry = tk.Entry(root)
    num_baixa_medica_entry.grid(row=14, column=1)

    inicio_contrato_label = tk.Label(root, text="Início do contrato:")
    inicio_contrato_label.grid(row=15, column=0)
    inicio_contrato_entry = tk.Entry(root)
    inicio_contrato_entry.grid(row=15, column=1)

    morada_label = tk.Label(root, text="Morada:")
    morada_label.grid(row=16, column=0)
    morada_entry = tk.Entry(root)
    morada_entry.grid(row=16, column=1)

    update_button = tk.Button(root, text="Atualizar", command=update_employee)
    update_button.grid(row=17, column=1)

def janela_deletar():
    def delete_employee():
        # Conecte-se ao banco de dados
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="78517231Le!",
            database="projeto"
        )
        cursor = db.cursor()

        # Prepare a consulta SQL
        sql = """
        DELETE FROM trabalhador WHERE id_trabalhador=%s
        """

        # Execute a consulta
        cursor.execute(sql, (id_entry.get(),))

        db.commit()

        messagebox.showinfo("Informação", "Funcionário deletado com sucesso")

    root = tk.Tk()

    # Crie um campo de entrada para o ID do funcionário
    id_label = tk.Label(root, text="ID do Funcionário:")
    id_label.grid(row=0, column=0)
    id_entry = tk.Entry(root)
    id_entry.grid(row=0, column=1)

    delete_button = tk.Button(root, text="Deletar Funcionário", command=delete_employee)
    delete_button.grid(row=1, column=1)

def janela_inserir_HISH():
    def update_hours():
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="78517231Le!",
            database="projeto"
        )
        cursor = db.cursor()

        # consulta SQL
        sql = """
        UPDATE historico_horas SET
        referencia_mes=%s,
        horas_trabalhadas=%s,
        horas_extras=%s,
        dias_baixa_medica=%s
        WHERE id_trabalhador=%s
        """

        # consulta
        cursor.execute(sql, (
            referencia_mes_entry.get(),
            horas_trabalhadas_entry.get(),
            horas_extras_entry.get(),
            dias_baixa_medica_entry.get(),
            id_trabalhador_entry.get()
        ))

        db.commit()

        messagebox.showinfo("Informação", "Horas do funcionário atualizadas com sucesso")

    root = tk.Tk()

    # campos de entrada para cada atributo
    id_trabalhador_label = tk.Label(root, text="ID do Trabalhador:")
    id_trabalhador_label.grid(row=0, column=0)
    id_trabalhador_entry = tk.Entry(root)
    id_trabalhador_entry.grid(row=0, column=1)

    referencia_mes_label = tk.Label(root, text="Referência do Mês:")
    referencia_mes_label.grid(row=1, column=0)
    referencia_mes_entry = tk.Entry(root)
    referencia_mes_entry.grid(row=1, column=1)

    horas_trabalhadas_label = tk.Label(root, text="Horas Trabalhadas:")
    horas_trabalhadas_label.grid(row=2, column=0)
    horas_trabalhadas_entry = tk.Entry(root)
    horas_trabalhadas_entry.grid(row=2, column=1)

    horas_extras_label = tk.Label(root, text="Horas Extras:")
    horas_extras_label.grid(row=3, column=0)
    horas_extras_entry = tk.Entry(root)
    horas_extras_entry.grid(row=3, column=1)

    dias_baixa_medica_label = tk.Label(root, text="Dias de Baixa Médica:")
    dias_baixa_medica_label.grid(row=4, column=0)
    dias_baixa_medica_entry = tk.Entry(root)
    dias_baixa_medica_entry.grid(row=4, column=1)


    update_button = tk.Button(root, text="Atualizar Horas", command=update_hours)
    update_button.grid(row=5, column=1)
def janela_atualizar_HISH():
    def update_hours():
        # Conecte-se ao banco de dados
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="78517231Le!",
            database="projeto"
        )
        cursor = db.cursor()

        # Prepare a consulta SQL
        sql = """
        UPDATE historico_horas SET
        referencia_mes=%s,
        horas_trabalhadas=%s,
        horas_extras=%s,
        dias_baixa_medica=%s
        WHERE id_trabalhador=%s
        """

        # Execute a consulta
        cursor.execute(sql, (
            referencia_mes_entry.get(),
            horas_trabalhadas_entry.get(),
            horas_extras_entry.get(),
            dias_baixa_medica_entry.get(),
            id_trabalhador_entry.get()
        ))

        db.commit()

        messagebox.showinfo("Informação", "Histórico de horas do funcionário atualizado com sucesso")

    root = tk.Tk()

    # Crie campos de entrada para cada atributo
    id_trabalhador_label = tk.Label(root, text="ID do Trabalhador:")
    id_trabalhador_label.grid(row=0, column=0)
    id_trabalhador_entry = tk.Entry(root)
    id_trabalhador_entry.grid(row=0, column=1)

    referencia_mes_label = tk.Label(root, text="Referência do Mês:")
    referencia_mes_label.grid(row=1, column=0)
    referencia_mes_entry = tk.Entry(root)
    referencia_mes_entry.grid(row=1, column=1)

    horas_trabalhadas_label = tk.Label(root, text="Horas Trabalhadas:")
    horas_trabalhadas_label.grid(row=2, column=0)
    horas_trabalhadas_entry = tk.Entry(root)
    horas_trabalhadas_entry.grid(row=2, column=1)

    horas_extras_label = tk.Label(root, text="Horas Extras:")
    horas_extras_label.grid(row=3, column=0)
    horas_extras_entry = tk.Entry(root)
    horas_extras_entry.grid(row=3, column=1)

    dias_baixa_medica_label = tk.Label(root, text="Dias de Baixa Médica:")
    dias_baixa_medica_label.grid(row=4, column=0)
    dias_baixa_medica_entry = tk.Entry(root)
    dias_baixa_medica_entry.grid(row=4, column=1)

    # Repita para todos os outros atributos...

    # Crie um botão para atualizar o histórico de horas
    update_button = tk.Button(root, text="Atualizar histórico de horas", command=update_hours)
    update_button.grid(row=5, column=1)

def janela_consulta_modificacao():
    def mostrar_modificacoes():
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="78517231Le!",
            database="projeto"
        )
        cursor = db.cursor()

        # Executa a consulta SQL
        cursor.execute("SELECT * FROM historico_modificacoes")

        # Obtém os dados
        info = cursor.fetchall()

        # Fecha a conexão
        db.close()

        return info

    # Função para criar a interface
    def janela_consulta_modificacoes(info):
        # Cria a janela Tkinter
        root = tk.Tk()
        root.title("Histórico de Modificações")
        root.geometry("1280x800")

        # Cria o Treeview com as colunas necessárias
        tree = ttk.Treeview(root, column=("c1", "c2", "c3", "c4", "c5"), show='headings')
        tree.column("#1" ,width=100, anchor=tk.CENTER)
        tree.heading("#1", text="ID da modificação")
        tree.column("#2",  width=170, anchor=tk.CENTER)
        tree.heading("#2", text="Data de modificação")
        tree.column("#3",  width=170, anchor=tk.CENTER)
        tree.heading("#3", text="ID do trabalhador modificado")
        tree.column("#4",  width=190, anchor=tk.CENTER)
        tree.heading("#4", text="ID do trabalhador que modificou")
        tree.column("#5",  width=700, anchor=tk.CENTER)
        tree.heading("#5", text="A Mudança")
        tree.pack()

        # Adiciona os dados ao Treeview
        for i in info:
            tree.insert("", 'end', values=i)

        # Inicia o loop Tkinter
        root.mainloop()

    # Obtém os dados
    info = mostrar_modificacoes()

    # Cria a interface
    janela_consulta_modificacoes(info)

def janela_deletar_modificacao():
    def delete_hours():
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="78517231Le!",
            database="projeto"
        )
        cursor = db.cursor()

        sql = """
        DELETE FROM historico_horas WHERE id_trabalhador=%s
        """

        # executar a consulta
        cursor.execute(sql, (id_trabalhador_entry.get(),))

        db.commit()

        messagebox.showinfo("Informação", "Histórico de horas do funcionário deletado com sucesso")

    root = tk.Tk()

    # campo de entrada para o ID do funcionário
    id_trabalhador_label = tk.Label(root, text="ID do Trabalhador:")
    id_trabalhador_label.grid(row=0, column=0)
    id_trabalhador_entry = tk.Entry(root)
    id_trabalhador_entry.grid(row=0, column=1)

    # botão para deletar o histórico de horas
    delete_button = tk.Button(root, text="Deletar Historico de horas", command=delete_hours)
    delete_button.grid(row=1, column=1)


root = tk.Tk()
root.title("Sistema de Gestão de Funcionários")
root.geometry("450x250")



open_button = tk.Button(root, text="Inserir dados do funcionário", command=novaJanela)
open_button.pack()

open_button1 = tk.Button(root, text="Atualizar dados do funcionário", command=janela_atualizar)
open_button1.pack()

open_button2 = tk.Button(root, text="Deletar dados do funcionário", command=janela_deletar)
open_button2.pack()

open_button3 = tk.Button(root, text="Inserir horas do funcionário", command=janela_inserir_HISH)
open_button3.pack()

open_button4 = tk.Button(root, text="Atualizar horas do funcionário", command=janela_atualizar_HISH)
open_button4.pack()

open_button5 = tk.Button(root, text="Calculadora de Salário", command=janela_salario)
open_button5.pack()

open_button6 = tk.Button(root, text="Histórico de Modificações", command=janela_consulta_modificacao)
open_button6.pack()

open_button7 = tk.Button(root, text="Deletar Histórico de Horas", command=janela_deletar_modificacao)
open_button7.pack()

root.mainloop()