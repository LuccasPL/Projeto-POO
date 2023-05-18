# calculo de salario, imposto e desconto, com base em horas trabalhadas e valor da hora, com base em uma classe
# criar uma classe salario para obter salarios diferentes de acordo com o estado civil, dependentes e salario.


class Salario:
    def __init__(self, estado_civil, dependentes, salario):
        self.estado_civil = estado_civil
        self.dependentes = dependentes
        self.salario = salario

    def descontos(self):
        if (self.salario <= 1500 and self.estado_civil == 'S'):
            return self.desconto_salario_1500_solteiro()
        elif (self.salario > 1500 and self.salario <= 2500 and self.estado_civil == 'S'):
            return self.desconto_salario_1500_2500_solteiro()
        elif (self.salario > 2500 and self.salario <= 3500 and self.estado_civil == 'S'):
            return self.desconto_salario_2500_3500_solteiro()
        elif (self.salario > 3500 and self.salario <= 4500 and self.estado_civil == 'S'):
            return self.desconto_salario_3500_4500_solteiro()
        elif (self.salario > 4500 and self.estado_civil == 'S'):
            return self.desconto_salario_4500_solteiro()
        elif (self.salario <= 1500 and self.estado_civil == 'C'):
            return self.desconto_salario_1500_casado()
        elif (self.salario > 1500 and self.salario <= 2500 and self.estado_civil == 'C'):
            return self.desconto_salario_1500_2500_casado()
        elif (self.salario > 2500 and self.salario <= 3500 and self.estado_civil == 'C'):
            return self.desconto_salario_2500_3500_casado()
        elif (self.salario > 3500 and self.salario <= 4500 and self.estado_civil == 'C'):
            return self.desconto_salario_3500_4500_casado()
        elif (self.salario > 4500 and self.estado_civil == 'C'):
            return self.desconto_salario_4500_casado()
        elif (self.salario <= 1500 and self.estado_civil == 'V'):
            return self.desconto_salario_1500_viuvo()
        elif (self.salario > 1500 and self.salario <= 2500 and self.estado_civil == 'V'):
            return self.desconto_salario_1500_2500_viuvo()
        elif (self.salario > 2500 and self.salario <= 3500 and self.estado_civil == 'V'):
            return self.desconto_salario_2500_3500_viuvo()
        elif (self.salario > 3500 and self.salario <= 4500 and self.estado_civil == 'V'):
            return self.desconto_salario_3500_4500_viuvo()
        elif (self.salario > 4500 and self.estado_civil == 'V'):
            return self.desconto_salario_4500_viuvo()
        elif (self.salario <= 1500 and self.estado_civil == 'D'):
            return self.desconto_salario_1500_divorciado()
        elif (self.salario > 1500 and self.salario <= 2500 and self.estado_civil == 'D'):
            return self.desconto_salario_1500_2500_divorciado()
        elif (self.salario > 2500 and self.salario <= 3500 and self.estado_civil == 'D'):
            return self.desconto_salario_2500_3500_divorciado()
        elif (self.salario > 3500 and self.salario <= 4500 and self.estado_civil == 'D'):
            return self.desconto_salario_3500_4500_divorciado()
        elif (self.salario > 4500 and self.estado_civil == 'D'):
            return self.desconto_salario_4500_divorciado()

    def desconto_salario_1500_solteiro(self):
        if (self.dependentes <= 1):
            return self.salario * 0.07
        elif (self.dependentes == 2):
            return self.salario * 0.05
        elif (self.dependentes == 3):
            return self.salario * 0.03
        elif (self.dependentes == 4):
            return self.salario * 0.01
        elif (self.dependentes >= 5):
            return self.salario * 0.00

    def desconto_salario_1500_2500_solteiro(self):
        if (self.dependentes <= 1):
            return self.salario * 0.06
        elif (self.dependentes == 2):
            return self.salario * 0.04
        elif (self.dependentes == 3):
            return self.salario * 0.02
        elif (self.dependentes == 4):
            return self.salario * 0.00
        elif (self.dependentes >= 5):
            return self.salario * 0.00

    def desconto_salario_2500_3500_solteiro(self):
        if (self.dependentes <= 1):
            return self.salario * 0.05
        elif (self.dependentes == 2):
            return self.salario * 0.03
        elif (self.dependentes == 3):
            return self.salario * 0.01
        elif (self.dependentes == 4):
            return self.salario * 0.00
        elif (self.dependentes >= 5):
            return self.salario * 0.00

    def desconto_salario_3500_4500_solteiro(self):
        if (self.dependentes <= 1):
            return self.salario * 0.0
        elif (self.dependentes == 2):
            return self.salario * 0.07
        elif (self.dependentes == 3):
            return self.salario * 0.05
        elif (self.dependentes == 4):
            return self.salario * 0.02
        elif (self.dependentes >= 5):
            return self.salario * 0.00

    def desconto_salario_4500_solteiro(self):
        if (self.dependentes <= 1):
            return self.salario * 0.09
        elif (self.dependentes == 2):
            return self.salario * 0.08
        elif (self.dependentes == 3):
            return self.salario * 0.06
        elif (self.dependentes == 4):
            return self.salario * 0.03
        elif (self.dependentes >= 5):
            return self.salario * 0.00

    #######################################################################################################################
    def desconto_salario_1500_casado(self):
        if (self.dependentes <= 1):
            return self.salario * 0.06
        elif (self.dependentes == 2):
            return self.salario * 0.05
        elif (self.dependentes == 3):
            return self.salario * 0.03
        elif (self.dependentes == 4):
            return self.salario * 0.01
        elif (self.dependentes >= 5):
            return self.salario * 0.00

    def desconto_salario_1500_2500_casado(self):
        if (self.dependentes <= 1):
            return self.salario * 0.05
        elif (self.dependentes == 2):
            return self.salario * 0.03
        elif (self.dependentes == 3):
            return self.salario * 0.01
        elif (self.dependentes == 4):
            return self.salario * 0.00
        elif (self.dependentes >= 5):
            return self.salario * 0.00

    def desconto_salario_2500_3500_casado(self):
        if (self.dependentes <= 1):
            return self.salario * 0.07
        elif (self.dependentes == 2):
            return self.salario * 0.05
        elif (self.dependentes == 3):
            return self.salario * 0.03
        elif (self.dependentes == 4):
            return self.salario * 0.01
        elif (self.dependentes >= 5):
            return self.salario * 0.00

    def desconto_salario_3500_4500_casado(self):
        if (self.dependentes <= 1):
            return self.salario * 0.08
        elif (self.dependentes == 2):
            return self.salario * 0.06
        elif (self.dependentes == 3):
            return self.salario * 0.04
        elif (self.dependentes == 4):
            return self.salario * 0.02
        elif (self.dependentes >= 5):
            return self.salario * 0.00

    def desconto_salario_4500_casado(self):
        if (self.dependentes <= 1):
            return self.salario * 0.09
        elif (self.dependentes == 2):
            return self.salario * 0.08
        elif (self.dependentes == 3):
            return self.salario * 0.06
        elif (self.dependentes == 4):
            return self.salario * 0.03
        elif (self.dependentes >= 5):
            return self.salario * 0.01

    #######################################################################################################################
    def desconto_salario_1500_viuvo(self):
        if (self.dependentes <= 1):
            return self.salario * 0.05
        elif (self.dependentes == 2):
            return self.salario * 0.04
        elif (self.dependentes == 3):
            return self.salario * 0.03
        elif (self.dependentes == 4):
            return self.salario * 0.02
        elif (self.dependentes >= 5):
            return self.salario * 0.01

    def desconto_salario_1500_2500_viuvo(self):
        if (self.dependentes <= 1):
            return self.salario * 0.04
        elif (self.dependentes == 2):
            return self.salario * 0.03
        elif (self.dependentes == 3):
            return self.salario * 0.02
        elif (self.dependentes == 4):
            return self.salario * 0.01
        elif (self.dependentes >= 5):
            return self.salario * 0.00

    def desconto_salario_2500_3500_viuvo(self):
        if (self.dependentes <= 1):
            return self.salario * 0.03
        elif (self.dependentes == 2):
            return self.salario * 0.02
        elif (self.dependentes == 3):
            return self.salario * 0.01
        elif (self.dependentes == 4):
            return self.salario * 0.00
        elif (self.dependentes >= 5):
            return self.salario * 0.00

    def desconto_salario_3500_4500_viuvo(self):
        if (self.dependentes <= 1):
            return self.salario * 0.02
        elif (self.dependentes == 2):
            return self.salario * 0.01
        elif (self.dependentes == 3):
            return self.salario * 0.00
        elif (self.dependentes == 4):
            return self.salario * 0.00
        elif (self.dependentes >= 5):
            return self.salario * 0.00

    def desconto_salario_4500_viuvo(self):
        if (self.dependentes <= 1):
            return self.salario * 0.07
        elif (self.dependentes == 2):
            return self.salario * 0.06
        elif (self.dependentes == 3):
            return self.salario * 0.05
        elif (self.dependentes == 4):
            return self.salario * 0.02
        elif (self.dependentes >= 5):
            return self.salario * 0.00

    #######################################################################################################################
    def desconto_salario_1500_divorciado(self):
        if (self.dependentes <= 1):
            return self.salario * 0.05
        elif (self.dependentes == 2):
            return self.salario * 0.04
        elif (self.dependentes == 3):
            return self.salario * 0.03
        elif (self.dependentes == 4):
            return self.salario * 0.02
        elif (self.dependentes >= 5):
            return self.salario * 0.01

    def desconto_salario_1500_2500_divorciado(self):
        if (self.dependentes <= 1):
            return self.salario * 0.04
        elif (self.dependentes == 2):
            return self.salario * 0.03
        elif (self.dependentes == 3):
            return self.salario * 0.02
        elif (self.dependentes == 4):
            return self.salario * 0.01
        elif (self.dependentes >= 5):
            return self.salario * 0.00

    def desconto_salario_2500_3500_divorciado(self):
        if (self.dependentes <= 1):
            return self.salario * 0.03
        elif (self.dependentes == 2):
            return self.salario * 0.02
        elif (self.dependentes == 3):
            return self.salario * 0.01
        elif (self.dependentes == 4):
            return self.salario * 0.00
        elif (self.dependentes >= 5):
            return self.salario * 0.00

    def desconto_salario_3500_4500_divorciado(self):
        if (self.dependentes <= 1):
            return self.salario * 0.02
        elif (self.dependentes == 2):
            return self.salario * 0.01
        elif (self.dependentes == 3):
            return self.salario * 0.00
        elif (self.dependentes == 4):
            return self.salario * 0.00
        elif (self.dependentes >= 5):
            return self.salario * 0.00

    def desconto_salario_4500_divorciado(self):
        if (self.dependentes <= 1):
            return self.salario * 0.08
        elif (self.dependentes == 2):
            return self.salario * 0.07
        elif (self.dependentes == 3):
            return self.salario * 0.06
        elif (self.dependentes == 4):
            return self.salario * 0.04
        elif (self.dependentes >= 5):
            return self.salario * 0.01

    #######################################################################################################################


class Funcionario:
    def __init__(self, nome, nif, nis, email, estadocivil, dependentes, departamento, cargo, horastrabalhadas,
                 valorhora,
                 horaextra, valorhoraextra, baixamedica, iniciocontrato, morada, observacoes):
        self.nome = nome
        self.nif = nif
        self.nis = nis
        self.email = email
        self.estadocivil = estadocivil
        self.dependentes = dependentes
        self.departamento = departamento
        self.cargo = cargo
        self.valorhora = valorhora
        self.horastrabalhadas = horastrabalhadas
        self.valorhoraextra = valorhoraextra
        self.horaextra = horaextra
        self.baixamedica = baixamedica
        self.iniciocontrato = iniciocontrato
        self.morada = morada
        self.observacoes = observacoes

    def load_from_db(self, conn, id):
        # TODO: SELECT a funcionarios.
        # self.nif = cur[1]
        pass

    def nif(self):
        return self.nif

    def nis(self):
        return self.nis

    def email(self):
        return self.email

    def estado_civil(self):
        if self.estadocivil == 'S':
            return 'Solteiro'
        elif self.estadocivil == 'C':
            return 'Casado'
        elif self.estadocivil == 'V':
            return 'Viúvo'
        elif self.estadocivil == 'D':
            return 'Divorciado'

    def departamento(self):
        return self.departamento

    def cargo(self):
        return self.cargo

    def valorhoraextra(self):
        return self.valorhoraextra

    def horaextra(self):
        return self.horaextra

    def baixamedica(self):
        return self.baixamedica

    def iniciocontrato(self):
        return self.iniciocontrato

    def observacoes(self):
        return self.observacoes

    def morada(self):
        return self.morada

    def salario(self):
        salario_base = self.horastrabalhadas * self.valorhora
        salario_extra = self.horaextra * self.valorhoraextra

        return salario_base + salario_extra

    def imposto_ssc(self):
        return self.salario() * 0.11

    def salario_liquido(self):
        return self.salario() - self.imposto_ssc()

    def desconto_salario(self):
        calc_salario = Salario(self.estadocivil, self.dependentes, self.salario())
        return calc_salario.descontos()

    def salvar_bd(self, conn):
        # TODO: INSERT INTO funcionarios whatever. self.nif, self.nis, etc.
        pass

    def __str__(self):
        return f'Nome: {self.nome}\nNIF: {self.nif}\nNIS: {self.nis}\nE-mail: {self.email}\nEstado Civil: {self.estado_civil}\nDependentes: {self.dependentes}\nDepartamento: {self.departamento}\nCargo: {self.cargo}\nImposto SSC: {self.imposto_ssc()}\nValor Hora Extra: {self.valorhoraextra}\nHoras Extra: {self.horaextra}\nBaixa Medica: {self.baixamedica}\nInício do Contrato: {self.iniciocontrato}\nMorada: {self.morada}\nObservações: {self.observacoes}\n'


print('Bem vindo ao sistema de cálculo de salario! \n')
nome = input('Digite o nome do funcionario: \n')
nif = int(input('Digite o NIF do funcionario: \n'))
nis = int(input('Digite o NIS do funcionario: \n'))
email = input('Digite o e-mail do funcionário: \n')
estadocivil = input('Digite o estado civil do funcionario: \n')
dependentes = int(input('Digite a quantidade de dependentes do funcionario: \n'))
departamento = input('Digite o departamento do funcionario: \n')
cargo = input('Digite o cargo do funcionario: \n')
horastrabalhadas = int(input('Digite a quantidade de horas trabalhadas até o momento: \n'))
valorhora = float(input('Digite o valor da hora trabalhada: \n'))
valorhoraextra = float(input('Digite o valor da hora extra: \n'))
horaextra = int(input('Digite a quantidade de horas extras até o momento: \n'))
baixamedica = int(input('Digite a quantidade de baixas medicas até o momento: \n'))
iniciocontrato = str(input('Digite a data de inicio do contrato: \n'))
morada = str(input('Digite a morada do funcionario: \n'))
observacoes = str(input('Digite as observações do funcionário: \n'))
print('----------------------------------------')
funcionario = Funcionario(nome, nif, nis, email, estadocivil, dependentes, departamento, cargo, horastrabalhadas,
                          valorhora,
                          horaextra, valorhoraextra, baixamedica, iniciocontrato, morada, observacoes)

print(funcionario)
print("Salario: " + str(funcionario.salario()))
print("Imposto SSC: " + str(funcionario.imposto_ssc()))
print("Salario Liquido: " + str(funcionario.salario_liquido()))
# funcionario.salvar_bd(conn)
