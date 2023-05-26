import tkinter as tk
import mysql.connector
from tkinter import messagebox
from tkinter import ttk

def imposto_ssc(salario):
    if salario <= 1000000:
        return 0.11

#funcao que vai calcular o desconto do salario dependendo do estado civil, numero de dependentes e salario
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
    # consulta SQL
    cursor.execute("SELECT estado_civil, num_dependentes, valor_hora, horas_trabalhadas, valor_hora_extra, horas_extras FROM trabalhador WHERE id_trabalhador=%s",
                   (id_trabalhador_entry.get(),))
    result = cursor.fetchone()

    if result is None:
        salario_label.config(text="Nenhum funcionário encontrado com o ID fornecido")
        return

    estado_civil, num_dependentes, valor_hora, horas_trabalhadas, valor_hora_extra, horas_extras = result
    # calcular o salario bruto
    salario = horas_trabalhadas * valor_hora + horas_extras * valor_hora_extra
    salario1= salario - (salario * imposto_ssc(salario))
    salario2 = salario1 - desconto(salario1, estado_civil, num_dependentes)

# formatar o salario para ter apenas 2 casas decimais
    salario2 = f"{salario2:.2f}"
    salario_label.config(text=f"O salário desse mes do funcionário é de {salario2} €")

def janela_salario():
    janela_salario = tk.Tk()

    global id_trabalhador_entry
    id_trabalhador_label = tk.Label(janela_salario, text="ID do Trabalhador:")
    id_trabalhador_label.grid(row=0, column=0)
    id_trabalhador_entry = tk.Entry(janela_salario)
    id_trabalhador_entry.grid(row=0, column=1)

    calculate_button = tk.Button(janela_salario, text="Calcular Salário", command=calcular_salario)
    calculate_button.grid(row=1, column=1)

    global salario_label
    salario_label = tk.Label(janela_salario, text="")
    salario_label.grid(row=2, column=0, columnspan=2)

def novaJanela():
    def inserir_funcionario():
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

        # Executa
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


    inserir_funcionario_inter = tk.Tk()
    inserir_funcionario_inter.title("Inserir dados do funcionário")

    nome_label = tk.Label(inserir_funcionario_inter, text="Nome:")
    nome_label.grid(row=0, column=0)
    nome_entry = tk.Entry(inserir_funcionario_inter)
    nome_entry.grid(row=0, column=1)

    senha_label = tk.Label(inserir_funcionario_inter, text="Senha:")
    senha_label.grid(row=1, column=0)
    senha_entry = tk.Entry(inserir_funcionario_inter)
    senha_entry.grid(row=1, column=1)

    nif_label = tk.Label(inserir_funcionario_inter, text="NIF:")
    nif_label.grid(row=2, column=0)
    nif_entry = tk.Entry(inserir_funcionario_inter)
    nif_entry.grid(row=2, column=1)

    niss_label = tk.Label(inserir_funcionario_inter, text="NISS:")
    niss_label.grid(row=3, column=0)
    niss_entry = tk.Entry(inserir_funcionario_inter)
    niss_entry.grid(row=3, column=1)

    email_label = tk.Label(inserir_funcionario_inter, text="Email:")
    email_label.grid(row=4, column=0)
    email_entry = tk.Entry(inserir_funcionario_inter)
    email_entry.grid(row=4, column=1)

    estado_civil_label = tk.Label(inserir_funcionario_inter, text="Estado Civil:")
    estado_civil_label.grid(row=5, column=0)
    estado_civil_entry = tk.Entry(inserir_funcionario_inter)
    estado_civil_entry.grid(row=5, column=1)

    num_dependentes_label = tk.Label(inserir_funcionario_inter, text="Número de dependentes:")
    num_dependentes_label.grid(row=6, column=0)
    num_dependentes_entry = tk.Entry(inserir_funcionario_inter)
    num_dependentes_entry.grid(row=6, column=1)

    departamento_label = tk.Label(inserir_funcionario_inter, text="Departamento:")
    departamento_label.grid(row=7, column=0)
    departamento_entry = tk.Entry(inserir_funcionario_inter)
    departamento_entry.grid(row=7, column=1)

    cargo_label = tk.Label(inserir_funcionario_inter, text="Cargo:")
    cargo_label.grid(row=8, column=0)
    cargo_entry = tk.Entry(inserir_funcionario_inter)
    cargo_entry.grid(row=8, column=1)

    valor_hora_label = tk.Label(inserir_funcionario_inter, text="Valor da hora:")
    valor_hora_label.grid(row=9, column=0)
    valor_hora_entry = tk.Entry(inserir_funcionario_inter)
    valor_hora_entry.grid(row=9, column=1)

    horas_trabalhadas_label = tk.Label(inserir_funcionario_inter, text="Horas trabalhadas:")
    horas_trabalhadas_label.grid(row=10, column=0)
    horas_trabalhadas_entry = tk.Entry(inserir_funcionario_inter)
    horas_trabalhadas_entry.grid(row=10, column=1)

    valor_hora_extra_label = tk.Label(inserir_funcionario_inter, text="Valor da hora extra:")
    valor_hora_extra_label.grid(row=11, column=0)
    valor_hora_extra_entry = tk.Entry(inserir_funcionario_inter)
    valor_hora_extra_entry.grid(row=11, column=1)

    horas_extras_label = tk.Label(inserir_funcionario_inter, text="Horas extras:")
    horas_extras_label.grid(row=12, column=0)
    horas_extras_entry = tk.Entry(inserir_funcionario_inter)
    horas_extras_entry.grid(row=12, column=1)

    num_baixa_medica_label = tk.Label(inserir_funcionario_inter, text="Número de baixas médicas:")
    num_baixa_medica_label.grid(row=13, column=0)
    num_baixa_medica_entry = tk.Entry(inserir_funcionario_inter)
    num_baixa_medica_entry.grid(row=13, column=1)

    inicio_contrato_label = tk.Label(inserir_funcionario_inter, text="Início do contrato:")
    inicio_contrato_label.grid(row=14, column=0)
    inicio_contrato_entry = tk.Entry(inserir_funcionario_inter)
    inicio_contrato_entry.grid(row=14, column=1)

    morada_label = tk.Label(inserir_funcionario_inter, text="Morada:")
    morada_label.grid(row=15, column=0)
    morada_entry = tk.Entry(inserir_funcionario_inter)
    morada_entry.grid(row=15, column=1)

    insert_button = tk.Button(inserir_funcionario_inter, text="Inserir Funcionário", command=inserir_funcionario)
    insert_button.grid(row=16, column=0, columnspan=2, pady=10, padx=10, ipadx=100)

def janela_atualizar():
    def atualizar_funcionario():
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="78517231Le!",
            database="projeto"
        )
        cursor = db.cursor()

        sql = """
        UPDATE trabalhador 
        SET nome=%s, senha=%s, num_nif=%s, num_niss=%s, email=%s, estado_civil=%s, num_dependentes=%s, departamento=%s, cargo=%s, valor_hora=%s, 
        horas_trabalhadas=%s, valor_hora_extra=%s, horas_extras=%s, num_baixa_medica=%s, inicio_contrato=%s, morada=%s
        WHERE id_trabalhador=%s
        """

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

    atualizar_funcionario_inter = tk.Tk()
    atualizar_funcionario_inter.title("Atualizar dados do funcionário")

    id_trabalhador_label = tk.Label(atualizar_funcionario_inter, text="ID do funcionário:")
    id_trabalhador_label.grid(row=0, column=0)
    id_trabalhador_entry = tk.Entry(atualizar_funcionario_inter)
    id_trabalhador_entry.grid(row=0, column=1)

    nome_label = tk.Label(atualizar_funcionario_inter, text="Nome:")
    nome_label.grid(row=1, column=0)
    nome_entry = tk.Entry(atualizar_funcionario_inter)
    nome_entry.grid(row=1, column=1)

    senha_label = tk.Label(atualizar_funcionario_inter, text="Senha:")
    senha_label.grid(row=2, column=0)
    senha_entry = tk.Entry(atualizar_funcionario_inter)
    senha_entry.grid(row=2, column=1)

    nif_label = tk.Label(atualizar_funcionario_inter, text="NIF:")
    nif_label.grid(row=3, column=0)
    nif_entry = tk.Entry(atualizar_funcionario_inter)
    nif_entry.grid(row=3, column=1)

    niss_label = tk.Label(atualizar_funcionario_inter, text="NISS:")
    niss_label.grid(row=4, column=0)
    niss_entry = tk.Entry(atualizar_funcionario_inter)
    niss_entry.grid(row=4, column=1)

    email_label = tk.Label(atualizar_funcionario_inter, text="Email:")
    email_label.grid(row=5, column=0)
    email_entry = tk.Entry(atualizar_funcionario_inter)
    email_entry.grid(row=5, column=1)

    estado_civil_label = tk.Label(atualizar_funcionario_inter, text="Estado civil:")
    estado_civil_label.grid(row=6, column=0)
    estado_civil_entry = tk.Entry(atualizar_funcionario_inter)
    estado_civil_entry.grid(row=6, column=1)

    num_dependentes_label = tk.Label(atualizar_funcionario_inter, text="Número de dependentes:")
    num_dependentes_label.grid(row=7, column=0)
    num_dependentes_entry = tk.Entry(atualizar_funcionario_inter)
    num_dependentes_entry.grid(row=7, column=1)

    departamento_label = tk.Label(atualizar_funcionario_inter, text="Departamento:")
    departamento_label.grid(row=8, column=0)
    departamento_entry = tk.Entry(atualizar_funcionario_inter)
    departamento_entry.grid(row=8, column=1)

    cargo_label = tk.Label(atualizar_funcionario_inter, text="Cargo:")
    cargo_label.grid(row=9, column=0)
    cargo_entry = tk.Entry(atualizar_funcionario_inter)
    cargo_entry.grid(row=9, column=1)

    valor_hora_label = tk.Label(atualizar_funcionario_inter, text="Valor da hora:")
    valor_hora_label.grid(row=10, column=0)
    valor_hora_entry = tk.Entry(atualizar_funcionario_inter)
    valor_hora_entry.grid(row=10, column=1)

    horas_trabalhadas_label = tk.Label(atualizar_funcionario_inter, text="Horas trabalhadas:")
    horas_trabalhadas_label.grid(row=11, column=0)
    horas_trabalhadas_entry = tk.Entry(atualizar_funcionario_inter)
    horas_trabalhadas_entry.grid(row=11, column=1)

    valor_hora_extra_label = tk.Label(atualizar_funcionario_inter, text="Valor da hora extra:")
    valor_hora_extra_label.grid(row=12, column=0)
    valor_hora_extra_entry = tk.Entry(atualizar_funcionario_inter)
    valor_hora_extra_entry.grid(row=12, column=1)

    horas_extras_label = tk.Label(atualizar_funcionario_inter, text="Horas extras:")
    horas_extras_label.grid(row=13, column=0)
    horas_extras_entry = tk.Entry(atualizar_funcionario_inter)
    horas_extras_entry.grid(row=13, column=1)

    num_baixa_medica_label = tk.Label(atualizar_funcionario_inter, text="Número de baixas médicas:")
    num_baixa_medica_label.grid(row=14, column=0)
    num_baixa_medica_entry = tk.Entry(atualizar_funcionario_inter)
    num_baixa_medica_entry.grid(row=14, column=1)

    inicio_contrato_label = tk.Label(atualizar_funcionario_inter, text="Início do contrato:")
    inicio_contrato_label.grid(row=15, column=0)
    inicio_contrato_entry = tk.Entry(atualizar_funcionario_inter)
    inicio_contrato_entry.grid(row=15, column=1)

    morada_label = tk.Label(atualizar_funcionario_inter, text="Morada:")
    morada_label.grid(row=16, column=0)
    morada_entry = tk.Entry(atualizar_funcionario_inter)
    morada_entry.grid(row=16, column=1)

    update_button = tk.Button(atualizar_funcionario_inter, text="Atualizar", command=atualizar_funcionario)
    update_button.grid(row=17, column=1)

def janela_deletar():
    def deletar_funcionario():
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="78517231Le!",
            database="projeto"
        )
        cursor = db.cursor()

        sql = """
        DELETE FROM trabalhador WHERE id_trabalhador=%s
        """

        cursor.execute(sql, (id_entry.get(),))

        db.commit()

        messagebox.showinfo("Informação", "Funcionário deletado com sucesso")

    deletar_funcionario_inter = tk.Tk()
    deletar_funcionario_inter.title("Deletar Funcionário")

    id_label = tk.Label(deletar_funcionario_inter, text="ID do Funcionário:")
    id_label.grid(row=0, column=0)
    id_entry = tk.Entry(deletar_funcionario_inter)
    id_entry.grid(row=0, column=1)

    delete_button = tk.Button(deletar_funcionario_inter, text="Deletar Funcionário", command=deletar_funcionario)
    delete_button.grid(row=1, column=1)

def janela_inserir_HISH():
    def atualizar_hora():
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="78517231Le!",
            database="projeto"
        )
        cursor = db.cursor()

        sql = """
        UPDATE historico_horas SET
        referencia_mes=%s,
        horas_trabalhadas=%s,
        horas_extras=%s,
        dias_baixa_medica=%s
        WHERE id_trabalhador=%s
        """

        cursor.execute(sql, (
            referencia_mes_entry.get(),
            horas_trabalhadas_entry.get(),
            horas_extras_entry.get(),
            dias_baixa_medica_entry.get(),
            id_trabalhador_entry.get()
        ))

        db.commit()

        messagebox.showinfo("Informação", "Horas do funcionário atualizadas com sucesso")

    atualizar_hora_inter = tk.Tk()
    atualizar_hora_inter.title("Inserir Horas")


    id_trabalhador_label = tk.Label(atualizar_hora_inter, text="ID do Trabalhador:")
    id_trabalhador_label.grid(row=0, column=0)
    id_trabalhador_entry = tk.Entry(atualizar_hora_inter)
    id_trabalhador_entry.grid(row=0, column=1)

    referencia_mes_label = tk.Label(atualizar_hora_inter, text="Referência do Mês:")
    referencia_mes_label.grid(row=1, column=0)
    referencia_mes_entry = tk.Entry(atualizar_hora_inter)
    referencia_mes_entry.grid(row=1, column=1)

    horas_trabalhadas_label = tk.Label(atualizar_hora_inter, text="Horas Trabalhadas:")
    horas_trabalhadas_label.grid(row=2, column=0)
    horas_trabalhadas_entry = tk.Entry(atualizar_hora_inter)
    horas_trabalhadas_entry.grid(row=2, column=1)

    horas_extras_label = tk.Label(atualizar_hora_inter, text="Horas Extras:")
    horas_extras_label.grid(row=3, column=0)
    horas_extras_entry = tk.Entry(atualizar_hora_inter)
    horas_extras_entry.grid(row=3, column=1)

    dias_baixa_medica_label = tk.Label(atualizar_hora_inter, text="Dias de Baixa Médica:")
    dias_baixa_medica_label.grid(row=4, column=0)
    dias_baixa_medica_entry = tk.Entry(atualizar_hora_inter)
    dias_baixa_medica_entry.grid(row=4, column=1)

    update_button = tk.Button(atualizar_hora_inter, text="Atualizar Horas", command=atualizar_hora)
    update_button.grid(row=5, column=1)
def janela_atualizar_HISH():
    def atualizar_horas():
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="78517231Le!",
            database="projeto"
        )
        cursor = db.cursor()


        sql = """
        UPDATE historico_horas SET
        referencia_mes=%s,
        horas_trabalhadas=%s,
        horas_extras=%s,
        dias_baixa_medica=%s
        WHERE id_trabalhador=%s
        """

        cursor.execute(sql, (
            referencia_mes_entry.get(),
            horas_trabalhadas_entry.get(),
            horas_extras_entry.get(),
            dias_baixa_medica_entry.get(),
            id_trabalhador_entry.get()
        ))

        db.commit()

        messagebox.showinfo("Informação", "Histórico de horas do funcionário atualizado com sucesso")

    atualizar_horas_inter = tk.Tk()
    atualizar_horas_inter.title("Atualizar Horas")

    id_trabalhador_label = tk.Label(atualizar_horas_inter, text="ID do Trabalhador:")
    id_trabalhador_label.grid(row=0, column=0)
    id_trabalhador_entry = tk.Entry(atualizar_horas_inter)
    id_trabalhador_entry.grid(row=0, column=1)

    referencia_mes_label = tk.Label(atualizar_horas_inter, text="Referência do Mês:")
    referencia_mes_label.grid(row=1, column=0)
    referencia_mes_entry = tk.Entry(atualizar_horas_inter)
    referencia_mes_entry.grid(row=1, column=1)

    horas_trabalhadas_label = tk.Label(atualizar_horas_inter, text="Horas Trabalhadas:")
    horas_trabalhadas_label.grid(row=2, column=0)
    horas_trabalhadas_entry = tk.Entry(atualizar_horas_inter)
    horas_trabalhadas_entry.grid(row=2, column=1)

    horas_extras_label = tk.Label(atualizar_horas_inter, text="Horas Extras:")
    horas_extras_label.grid(row=3, column=0)
    horas_extras_entry = tk.Entry(atualizar_horas_inter)
    horas_extras_entry.grid(row=3, column=1)

    dias_baixa_medica_label = tk.Label(atualizar_horas_inter, text="Dias de Baixa Médica:")
    dias_baixa_medica_label.grid(row=4, column=0)
    dias_baixa_medica_entry = tk.Entry(atualizar_horas_inter)
    dias_baixa_medica_entry.grid(row=4, column=1)


    update_button = tk.Button(atualizar_horas_inter, text="Atualizar histórico de horas", command=atualizar_horas)
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

        cursor.execute("SELECT * FROM historico_modificacoes")

        info = cursor.fetchall()

        db.close()

        return info

    # Função para criar a interface
    def janela_consulta_modificacoes(info):

        mostrar_modificacoes_inter = tk.Tk()
        mostrar_modificacoes_inter.title("Histórico de Modificações")
        mostrar_modificacoes_inter.geometry("1280x800")

        tree = ttk.Treeview(mostrar_modificacoes_inter, column=("c1", "c2", "c3", "c4", "c5"), show='headings')
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

        for i in info:
            tree.insert("", 'end', values=i)

        mostrar_modificacoes_inter.mainloop()

    info = mostrar_modificacoes()

    janela_consulta_modificacoes(info)

def janela_deletar_modificacao():
    def deletar_horas():
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

        #  consulta
        cursor.execute(sql, (id_trabalhador_entry.get(),))

        db.commit()

        messagebox.showinfo("Informação", "Histórico de horas do funcionário deletado com sucesso")

    deletar_horas_inter = tk.Tk()
    deletar_horas_inter.title("Deletar Horas")

    id_trabalhador_label = tk.Label(deletar_horas_inter, text="ID do Trabalhador:")
    id_trabalhador_label.grid(row=0, column=0)
    id_trabalhador_entry = tk.Entry(deletar_horas_inter)
    id_trabalhador_entry.grid(row=0, column=1)

    delete_button = tk.Button(deletar_horas_inter, text="Deletar Historico de horas", command=deletar_horas)
    delete_button.grid(row=1, column=1)


def interface_consultar_funcionarios():
    def mostrar_funcionario():
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="78517231Le!",
            database="projeto"
        )
        cursor = db.cursor()

        cursor.execute("SELECT * FROM trabalhador")

        info = cursor.fetchall()

        db.close()

        return info


    def janela_consulta_funcionarios(info):

        consultar_funcionarios_inter = tk.Toplevel()
        consultar_funcionarios_inter.title("Funcionários")
        consultar_funcionarios_inter.geometry("1280x800")

        tree = ttk.Treeview(consultar_funcionarios_inter, column=("c1", "c2", "c3", "c4", "c5", 'c6', "c7", "c8", "c9", "c10", "c11", "c12", "c13", "c14", "c15", "c16", "c17"), show='headings')
        tree.column("#1", width=80, anchor=tk.CENTER)
        tree.heading("#1", text="ID do trabalhador")
        tree.column("#2", width=200, anchor=tk.CENTER)
        tree.heading("#2", text="Nome")
        tree.column("#3", width=120, anchor=tk.CENTER)
        tree.heading("#3", text="Senha")
        tree.column("#4", width=170, anchor=tk.CENTER)
        tree.heading("#4", text="NIF")
        tree.column("#5", width=170, anchor=tk.CENTER)
        tree.heading("#5", text="NIS")
        tree.column("#6", width=250, anchor=tk.CENTER)
        tree.heading("#6", text="E-mail")
        tree.column("#7", width=100, anchor=tk.CENTER)
        tree.heading("#7", text="Estado Civil")
        tree.column("#8", width=130, anchor=tk.CENTER)
        tree.heading("#8", text="Número de dependentes")
        tree.column("#9", width=150, anchor=tk.CENTER)
        tree.heading("#9", text="Departamento")
        tree.column("#10", width=150, anchor=tk.CENTER)
        tree.heading("#10", text="Cargo")
        tree.column("#11", width=120, anchor=tk.CENTER)
        tree.heading("#11", text="Horas Trabalhadas")
        tree.column("#12", width=120, anchor=tk.CENTER)
        tree.heading("#12", text="Valor da hora")
        tree.column("#13", width=150, anchor=tk.CENTER)
        tree.heading("#13", text="Valor da hora extra")
        tree.column("#14", width=120, anchor=tk.CENTER)
        tree.heading("#14", text="Horas extras")
        tree.column("#15", width=150, anchor=tk.CENTER)
        tree.heading("#15", text="Número de baixas médicas")
        tree.column("#16", width=230, anchor=tk.CENTER)
        tree.heading("#16", text="Início do contrato")
        tree.column("#17", width=250, anchor=tk.CENTER)
        tree.heading("#17", text="Morada")


        tree.pack()

        for i in info:
            tree.insert("", 'end', values=i)

        consultar_funcionarios_inter.mainloop()

    info = mostrar_funcionario()

    janela_consulta_funcionarios(info)

def interface_consultar_horas():
    def mostrar_modificacoes():
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="78517231Le!",
            database="projeto"
        )
        cursor = db.cursor()

        cursor.execute("SELECT * FROM historico_horas")

        info = cursor.fetchall()

        db.close()

        return info


    def janela_consulta_horas(info):

        consulta_horas_inter = tk.Toplevel()
        consulta_horas_inter.title("Historico de horas")
        consulta_horas_inter.geometry("1280x800")

        tree = ttk.Treeview(consulta_horas_inter, column=("c1", "c2", "c3", "c4", "c5", 'c6'), show='headings')
        tree.column("#1", width=130, anchor=tk.CENTER)
        tree.heading("#1", text="ID historico de horas")
        tree.column("#2",  width=100, anchor=tk.CENTER)
        tree.heading("#2", text="ID trabalhador")
        tree.column("#3",  width=120, anchor=tk.CENTER)
        tree.heading("#3", text="Referencia do mês")
        tree.column("#4", width=150, anchor=tk.CENTER)
        tree.heading("#4", text="Horas trabalhadas")
        tree.column("#5", width=150, anchor=tk.CENTER)
        tree.heading("#5", text="Horas extras")
        tree.column("#6", width=150, anchor=tk.CENTER)
        tree.heading("#6", text="Dias de baixa médica")

        tree.pack()

        for i in info:
            tree.insert("", 'end', values=i)

        consulta_horas_inter.mainloop()

    info = mostrar_modificacoes()

    janela_consulta_horas(info)

def interface_principal(tipo):
    interface_principal = tk.Tk()
    interface_principal.title("Sistema de Gestão de Funcionários")
    interface_principal.geometry("450x320")

    open_button = tk.Button(interface_principal, text="Inserir dados do funcionário", command=novaJanela, state=tk.DISABLED)
    open_button1 = tk.Button(interface_principal, text="Atualizar dados do funcionário", command=janela_atualizar, state=tk.DISABLED)
    open_button2 = tk.Button(interface_principal, text="Deletar dados do funcionário", command=janela_deletar, state=tk.DISABLED)
    open_button3 = tk.Button(interface_principal, text="Inserir horas do funcionário", command=janela_inserir_HISH, state=tk.DISABLED)
    open_button4 = tk.Button(interface_principal, text="Atualizar horas do funcionário", command=janela_atualizar_HISH, state=tk.DISABLED)
    open_button5 = tk.Button(interface_principal, text="Calculadora de Salário", command=janela_salario, state=tk.DISABLED)
    open_button6 = tk.Button(interface_principal, text="Histórico de Modificações", command=janela_consulta_modificacao, state=tk.DISABLED)
    open_button7 = tk.Button(interface_principal, text="Deletar Histórico de Horas", command=janela_deletar_modificacao, state=tk.DISABLED)
    open_button8 = tk.Button(interface_principal, text="Consultar Funcionários", command=interface_consultar_funcionarios, state=tk.DISABLED)
    open_button9 = tk.Button(interface_principal, text="Consultar Horas", command=interface_consultar_horas, state=tk.DISABLED)
    sair_button = tk.Button(interface_principal, text="Sair", command=interface_principal.destroy)
    sair_button.pack(side=tk.BOTTOM)


    if tipo == 'gerente':
        open_button.config(state=tk.NORMAL)
        open_button1.config(state=tk.NORMAL)
        open_button2.config(state=tk.NORMAL)
        open_button3.config(state=tk.NORMAL)
        open_button4.config(state=tk.NORMAL)
        open_button5.config(state=tk.NORMAL)
        open_button6.config(state=tk.NORMAL)
        open_button7.config(state=tk.NORMAL)
        open_button8.config(state=tk.NORMAL)
        open_button9.config(state=tk.NORMAL)
    elif tipo == 'funcionario':
        open_button8.config(state=tk.NORMAL)
        open_button9.config(state=tk.NORMAL)
    elif tipo == 'auditoria':
        open_button5.config(state=tk.NORMAL)
        open_button6.config(state=tk.NORMAL)
        open_button8.config(state=tk.NORMAL)
        open_button9.config(state=tk.NORMAL)

    open_button.pack()
    open_button1.pack()
    open_button2.pack()
    open_button3.pack()
    open_button4.pack()
    open_button5.pack()
    open_button6.pack()
    open_button7.pack()
    open_button8.pack()
    open_button9.pack()

    interface_principal.mainloop()

def login(db, username, senha):
    cursor = db.cursor()
    try:
        cursor.execute("SELECT tipo FROM usuarios WHERE username = %s AND senha = %s", (username, senha))
        result = cursor.fetchone()

        if result is None:
            messagebox.showerror("Erro", "Usuário ou senha inválidos")
        else:
            tipo = result[0]
            if tipo == 'gerente':
                messagebox.showinfo("Sucesso", "Bem-vindo, gerente!")


            elif tipo == 'funcionario':
                messagebox.showinfo("Sucesso", "Bem-vindo, funcionário!")


            elif tipo == 'auditoria':
                messagebox.showinfo("Sucesso", "Bem-vindo, auditoria!")
                

            else:
                messagebox.showerror("Erro", "Tipo de usuário desconhecido")

            interface_principal(tipo)

    except mysql.connector.Error as err:
        messagebox.showerror("Erro", f"Erro ao fazer login: {err}")

    finally:

        cursor.close()

def criar_interface_login(db):
    login_inter = tk.Tk()
    login_inter.title("Login")
    login_inter.geometry("220x100")

    frm = ttk.Frame(login_inter, padding=10)
    frm.grid()

    lbl_username = ttk.Label(frm, text="Usuário:")
    lbl_senha = ttk.Label(frm, text="Senha:")
    lbl_username.grid(row=0, column=0, sticky="W")
    lbl_senha.grid(row=1, column=0, sticky="W")

    username = tk.StringVar()
    txt_username = ttk.Entry(frm, width=15, textvariable=username)
    txt_username.grid(row=0, column=1)

    senha = tk.StringVar()
    txt_senha = ttk.Entry(frm, width=15, textvariable=senha, show="*")
    txt_senha.grid(row=1, column=1)

    btn_login = ttk.Button(frm, text="Login", command=lambda: login(db, username.get(), senha.get()))
    btn_login.grid(row=2, column=1, sticky="W")

    login_inter.mainloop()

db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="78517231Le!",
        database="projeto"
    )

criar_interface_login(db)





# LOGINS: gerente, funcionario, auditoria
# gerente1, senha: 55a5e9e78207b4df8699d60886fa070079463547b095d1a05bc719bb4e6cd251
# funcionario1, senha: 6b08d780140e292a4af8ba3f2333fc1357091442d7e807c6cad92e8dcd0240b7
# auditoria1, senha: b578dc5fcbfabbc7e96400601d0858c951f04929faef033bbbc117ab935c6ae9



