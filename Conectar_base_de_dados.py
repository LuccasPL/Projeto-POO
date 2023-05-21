import mysql.connector


# Conectando ao banco de dados
conn = mysql.connector.connect(host= 'localhost', database = "projeto", user = "root", password = "78517231Le!")

# funcao que pesquisa e retorna os dados de todos os funcionarios
def todos_os_trabalhadores():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM trabalhador")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows


# funcao que pesquisa e retorna os dados de um funcionario digitando apenas o nome
def trabalhador_por_nome(nome):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM trabalhador WHERE nome = %s", (nome,))
    rows = cursor.fetchone()
    cursor.close()
    conn.close()
    return rows

# uma funcao que pesquisa e retorna os dados de um funcionario digitando apenas o ID
def trabalhador_por_id(id_trabalhador):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM trabalhador WHERE id_trabalhador = %s", (id_trabalhador,))
    rows = cursor.fetchone()
    cursor.close()
    conn.close()
    return rows

# funcao que pesquisa e retorna todos os funcionarios de um departamento
def trabalhador_por_departamento(departamento):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM trabalhador WHERE departamento = %s", (departamento,))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

# funcao que pesquisa e retorna todos os funcionarios de um estado civil
def trabalhador_por_estado_civil(estado_civil):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM trabalhador WHERE estado_civil = %s", (estado_civil,))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

# funcao que pesquisa e retorna o historico de horas trabalhadas de um funcionario
def historico_horas_trabalhadas(id_trabalhador):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM historico_horas WHERE id_trabalhador = %s", (id_trabalhador,))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

# funcao que adiciona um novo funcionario
def adicionar_trabalhador(nome, senha, num_nif, num_niss, email, estado_civil, num_dependentes, departamento, cargo, valor_hora,horas_trabalhadas,
                          valor_hora_extra,horas_extras,num_baixa_medica, inicio_contrato, morada):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO trabalhador (nome, senha, num_nif, num_niss, email, estado_civil, num_dependentes, departamento, cargo, valor_hora,"
                   "horas_trabalhadas, valor_hora_extra,horas_extras,num_baixa_medica, inicio_contrato, morada) "
                   "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                   (nome, senha, num_nif, num_niss, email, estado_civil, num_dependentes, departamento, cargo, valor_hora,horas_trabalhadas,
                    valor_hora_extra,horas_extras,num_baixa_medica, inicio_contrato, morada))
    conn.commit()
    cursor.close()
    conn.close()


# funcao que atualiza os dados de um funcionario
def atualizar_trabalhador(id_trabalhador, nome, senha, num_nif, num_niss, email, estado_civil, num_dependentes, departamento, cargo, valor_hora,horas_trabalhadas,
                            valor_hora_extra,horas_extras,num_baixa_medica, inicio_contrato, morada):
        cursor = conn.cursor()
        cursor.execute("UPDATE trabalhador SET nome = %s, senha = %s, num_nif = %s, num_niss = %s, email = %s, estado_civil = %s, num_dependentes = %s, departamento = %s, cargo = %s, valor_hora = %s,"
                     "horas_trabalhadas = %s, valor_hora_extra = %s,horas_extras = %s,num_baixa_medica = %s, inicio_contrato = %s, morada = %s WHERE id_trabalhador = %s",
                     (nome, senha, num_nif, num_niss, email, estado_civil, num_dependentes, departamento, cargo, valor_hora,horas_trabalhadas,
                        valor_hora_extra,horas_extras,num_baixa_medica, inicio_contrato, morada, id_trabalhador))
        conn.commit()
        cursor.close()
        conn.close()

# funcao que deleta um funcionario
def deletar_trabalhador(id_trabalhador):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM trabalhador WHERE id = %s", (id_trabalhador,))
    conn.commit()
    cursor.close()
    conn.close()

#funcao que pesquisa e retorna o historico de modificacoes de um funcionario
def historico_modificacoes(id_trabalhador):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM historico_modificacoes WHERE id_trabalhador = %s", (id_trabalhador,))
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

