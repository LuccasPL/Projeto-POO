# calculo de salario, imposto e desconto, com base em horas trabalhadas e valor da hora, com base em uma classe
# criar uma classe salario para obter salarios diferentes de acordo com o estado civil, dependentes e salario.


class Salario:
    def __init__(self, estado_civil, dependentes, salario):
        self.estado_civil = estado_civil
        self.dependentes = dependentes
        self.salario = salario

    def desconto_salario_1500_solteiro(self):
        if (self.dependentes <= 1 and self.salario <= 1500 and self.estado_civil == 'S'):
            return self.salario * 0.07
        elif (self.dependentes == 2 and self.salario <= 1500 and self.estado_civil == 'S'):
            return self.salario * 0.05
        elif (self.dependentes == 3 and self.salario <= 1500 and self.estado_civil == 'S'):
            return self.salario * 0.03
        elif (self.dependentes == 4 and self.salario <= 1500 and self.estado_civil == 'S'):
            return self.salario * 0.01
        elif (self.dependentes >= 5 and self.salario <= 1500 and self.estado_civil == 'S'):
            return self.salario * 0.00

    def desconto_salario_1500_2500_solteiro(self):
        if (self.dependentes <= 1 and self.salario > 1500 and self.salario <= 2500 and self.estado_civil == 'S'):
            return self.salario * 0.06
        elif (self.dependentes == 2 and self.salario > 1500 and self.salario <= 2500 and self.estado_civil == 'S'):
            return self.salario * 0.04
        elif (self.dependentes == 3 and self.salario > 1500 and self.salario <= 2500 and self.estado_civil == 'S'):
            return self.salario * 0.02
        elif (self.dependentes == 4 and self.salario > 1500 and self.salario <= 2500 and self.estado_civil == 'S'):
            return self.salario * 0.00
        elif (self.dependentes >= 5 and self.salario > 1500 and self.salario <= 2500 and self.estado_civil == 'S'):
            return self.salario * 0.00

    def desconto_salario_2500_3500_solteiro(self):
        if (self.dependentes <= 1 and self.salario > 2500 and self.salario <= 3500 and self.estado_civil == 'S'):
            return self.salario * 0.07
        elif (self.dependentes == 2 and self.salario > 2500 and self.salario <= 3500 and self.estado_civil == 'S'):
            return self.salario * 0.06
        elif (self.dependentes == 3 and self.salario > 2500 and self.salario <= 3500 and self.estado_civil == 'S'):
            return self.salario * 0.04
        elif (self.dependentes == 4 and self.salario > 2500 and self.salario <= 3500 and self.estado_civil == 'S'):
            return self.salario * 0.02
        elif (self.dependentes >= 5 and self.salario > 2500 and self.salario <= 3500 and self.estado_civil == 'S'):
            return self.salario * 0.00

    def desconto_salario_3500_4500_solteiro(self):
        if (self.dependentes <= 1 and self.salario > 3500 and self.salario <= 4500 and self.estado_civil == 'S'):
            return self.salario * 0.08
        elif (self.dependentes == 2 and self.salario > 3500 and self.salario <= 4500 and self.estado_civil == 'S'):
            return self.salario * 0.07
        elif (self.dependentes == 3 and self.salario > 3500 and self.salario <= 4500 and self.estado_civil == 'S'):
            return self.salario * 0.05
        elif (self.dependentes == 4 and self.salario > 3500 and self.salario <= 4500 and self.estado_civil == 'S'):
            return self.salario * 0.02
        elif (self.dependentes >= 5 and self.salario > 3500 and self.salario <= 4500 and self.estado_civil == 'S'):
            return self.salario * 0.00

    def desconto_salario_4500_solteiro(self):
        if (self.dependentes <= 1 and self.salario > 4500 and self.estado_civil == 'S'):
            return self.salario * 0.09
        elif (self.dependentes == 2 and self.salario > 4500 and self.estado_civil == 'S'):
            return self.salario * 0.08
        elif (self.dependentes == 3 and self.salario > 4500 and self.estado_civil == 'S'):
            return self.salario * 0.06
        elif (self.dependentes == 4 and self.salario > 4500 and self.estado_civil == 'S'):
            return self.salario * 0.03
        elif (self.dependentes >= 5 and self.salario > 4500 and self.estado_civil == 'S'):
            return self.salario * 0.00
#######################################################################################################################
    def desconto_salario_1500_casado(self):
        if (self.dependentes <= 1 and self.salario <= 1500 and self.estado_civil == 'C'):
            return self.salario * 0.06
        elif (self.dependentes == 2 and self.salario <= 1500 and self.estado_civil == 'C'):
            return self.salario * 0.05
        elif (self.dependentes == 3 and self.salario <= 1500 and self.estado_civil == 'C'):
            return self.salario * 0.03
        elif (self.dependentes == 4 and self.salario <= 1500 and self.estado_civil == 'C'):
            return self.salario * 0.01
        elif (self.dependentes >= 5 and self.salario <= 1500 and self.estado_civil == 'C'):
            return self.salario * 0.00

    def desconto_salario_1500_2500_casado(self):
        if (self.dependentes <= 1 and self.salario > 1500 and self.salario <= 2500 and self.estado_civil == 'C'):
            return self.salario * 0.06
        elif (self.dependentes == 2 and self.salario > 1500 and self.salario <= 2500 and self.estado_civil == 'C'):
            return self.salario * 0.04
        elif (self.dependentes == 3 and self.salario > 1500 and self.salario <= 2500 and self.estado_civil == 'C'):
            return self.salario * 0.02
        elif (self.dependentes == 4 and self.salario > 1500 and self.salario <= 2500 and self.estado_civil == 'C'):
            return self.salario * 0.01
        elif (self.dependentes >= 5 and self.salario > 1500 and self.salario <= 2500 and self.estado_civil == 'C'):
            return self.salario * 0.00

    def desconto_salario_2500_3500_casado(self):
        if (self.dependentes <= 1 and self.salario > 2500 and self.salario <= 3500 and self.estado_civil == 'C'):
            return self.salario * 0.07
        elif (self.dependentes == 2 and self.salario > 2500 and self.salario <= 3500 and self.estado_civil == 'C'):
            return self.salario * 0.05
        elif (self.dependentes == 3 and self.salario > 2500 and self.salario <= 3500 and self.estado_civil == 'C'):
            return self.salario * 0.03
        elif (self.dependentes == 4 and self.salario > 2500 and self.salario <= 3500 and self.estado_civil == 'C'):
            return self.salario * 0.01
        elif (self.dependentes >= 5 and self.salario > 2500 and self.salario <= 3500 and self.estado_civil == 'C'):
            return self.salario * 0.00

    def desconto_salario_3500_4500_casado(self):
        if (self.dependentes <= 1 and self.salario > 3500 and self.salario <= 4500 and self.estado_civil == 'C'):
            return self.salario * 0.08
        elif (self.dependentes == 2 and self.salario > 3500 and self.salario <= 4500 and self.estado_civil == 'C'):
            return self.salario * 0.06
        elif (self.dependentes == 3 and self.salario > 3500 and self.salario <= 4500 and self.estado_civil == 'C'):
            return self.salario * 0.04
        elif (self.dependentes == 4 and self.salario > 3500 and self.salario <= 4500 and self.estado_civil == 'C'):
            return self.salario * 0.02
        elif (self.dependentes >= 5 and self.salario > 3500 and self.salario <= 4500 and self.estado_civil == 'C'):
            return self.salario * 0.00

    def desconto_salario_4500_casado(self):
        if (self.dependentes <= 1 and self.salario > 4500 and self.estado_civil == 'C'):
            return self.salario * 0.09
        elif (self.dependentes == 2 and self.salario > 4500 and self.estado_civil == 'C'):
            return self.salario * 0.07
        elif (self.dependentes == 3 and self.salario > 4500 and self.estado_civil == 'C'):
            return self.salario * 0.05
        elif (self.dependentes == 4 and self.salario > 4500 and self.estado_civil == 'C'):
            return self.salario * 0.03
        elif (self.dependentes >= 5 and self.salario > 4500 and self.estado_civil == 'C'):
            return self.salario * 0.01
    #######################################################################################################################
    def desconto_salario_1500_viuvo(self):
        if (self.dependentes <= 1 and self.salario <= 1500 and self.estado_civil == 'V'):
            return self.salario * 0.05
        elif (self.dependentes == 2 and self.salario <= 1500 and self.estado_civil == 'V'):
            return self.salario * 0.04
        elif (self.dependentes == 3 and self.salario <= 1500 and self.estado_civil == 'V'):
            return self.salario * 0.03
        elif (self.dependentes == 4 and self.salario <= 1500 and self.estado_civil == 'V'):
            return self.salario * 0.02
        elif (self.dependentes >= 5 and self.salario <= 1500 and self.estado_civil == 'V'):
            return self.salario * 0.01

    def desconto_salario_1500_2500_viuvo(self):
        if (self.dependentes <= 1 and self.salario > 1500 and self.salario <= 2500 and self.estado_civil == 'V'):
            return self.salario * 0.04
        elif (self.dependentes == 2 and self.salario > 1500 and self.salario <= 2500 and self.estado_civil == 'V'):
            return self.salario * 0.03
        elif (self.dependentes == 3 and self.salario > 1500 and self.salario <= 2500 and  self.estado_civil == 'V'):
            return self.salario * 0.02
        elif (self.dependentes == 4 and self.salario > 1500 and self.salario <= 2500 and  self.estado_civil == 'V'):
            return self.salario * 0.01
        elif (self.dependentes >= 5 and self.salario > 1500 and self.salario <= 2500 and self.estado_civil == 'V'):
            return self.salario * 0.00

    def desconto_salario_2500_3500_viuvo(self):
        if (self.dependentes <= 1 and self.salario > 2500 and self.salario <= 3500 and self.estado_civil == 'V'):
            return self.salario * 0.03
        elif (self.dependentes == 2 and self.salario > 2500 and self.salario <= 3500 and self.estado_civil == 'V'):
            return self.salario * 0.02
        elif (self.dependentes == 3 and self.salario > 2500 and self.salario <= 3500 and self.estado_civil == 'V'):
            return self.salario * 0.01
        elif (self.dependentes == 4 and self.salario > 2500 and self.salario <= 3500 and self.estado_civil == 'V'):
            return self.salario * 0.00
        elif (self.dependentes >= 5 and self.salario > 2500 and self.salario <= 3500 and self.estado_civil == 'V'):
            return self.salario * 0.00

    def desconto_salario_3500_4500_viuvo(self):
        if (self.dependentes <= 1 and self.salario > 3500 and self.salario <= 4500 and self.estado_civil == 'V'):
            return self.salario * 0.02
        elif (self.dependentes == 2 and self.salario > 3500 and self.salario <= 4500 and self.estado_civil == 'V'):
            return self.salario * 0.01
        elif (self.dependentes == 3 and self.salario > 3500 and self.salario <= 4500 and self.estado_civil == 'V'):
            return self.salario * 0.00
        elif (self.dependentes == 4 and self.salario > 3500 and self.salario <= 4500 and self.estado_civil == 'V'):
            return self.salario * 0.00
        elif (self.dependentes >= 5 and self.salario > 3500 and self.salario <= 4500 and self.estado_civil == 'V'):
            return self.salario * 0.00

    def desconto_salario_4500_viuvo(self):
        if (self.dependentes <= 1 and self.salario > 4500 and self.estado_civil == 'V'):
            return self.salario * 0.07
        elif (self.dependentes == 2 and self.salario > 4500 and self.estado_civil == 'V'):
            return self.salario * 0.06
        elif (self.dependentes == 3 and self.salario > 4500 and self.estado_civil == 'V'):
            return self.salario * 0.05
        elif (self.dependentes == 4 and self.salario > 4500 and self.estado_civil == 'V'):
            return self.salario * 0.02
        elif (self.dependentes >= 5 and self.salario > 4500 and self.estado_civil == 'V'):
            return self.salario * 0.00
    #######################################################################################################################
    def desconto_salario_1500_divorciado(self):
        if (self.dependentes <= 1 and self.salario <= 1500 and self.estado_civil == 'D'):
            return self.salario * 0.05
        elif (self.dependentes == 2 and self.salario <= 1500 and self.estado_civil == 'D'):
            return self.salario * 0.04
        elif (self.dependentes == 3 and self.salario <= 1500 and self.estado_civil == 'D'):
            return self.salario * 0.03
        elif (self.dependentes == 4 and self.salario <= 1500 and self.estado_civil == 'D'):
            return self.salario * 0.02
        elif (self.dependentes >= 5 and self.salario <= 1500 and self.estado_civil == 'D'):
            return self.salario * 0.01

    def desconto_salario_1500_2500_divorciado(self):
        if (self.dependentes <= 1 and self.salario > 1500 and self.salario <= 2500 and self.estado_civil == 'D'):
            return self.salario * 0.04
        elif (self.dependentes == 2 and self.salario > 1500 and self.salario <= 2500 and self.estado_civil == 'D'):
            return self.salario * 0.03
        elif (self.dependentes == 3 and self.salario > 1500 and self.salario <= 2500 and self.estado_civil == 'D'):
            return self.salario * 0.02
        elif (self.dependentes == 4 and self.salario > 1500 and self.salario <= 2500 and self.estado_civil == 'D'):
            return self.salario * 0.01
        elif (self.dependentes >= 5 and self.salario > 1500 and self.salario <= 2500 and self.estado_civil == 'D'):
            return self.salario * 0.00

    def desconto_salario_2500_3500_divorciado(self):
        if (self.dependentes <= 1 and self.salario > 2500 and self.salario <= 3500 and self.estado_civil == 'D'):
            return self.salario * 0.03
        elif (self.dependentes == 2 and self.salario > 2500 and self.salario <= 3500 and self.estado_civil == 'D'):
            return self.salario * 0.02
        elif (self.dependentes == 3 and self.salario > 2500 and self.salario <= 3500 and self.estado_civil == 'D'):
            return self.salario * 0.01
        elif (self.dependentes == 4 and self.salario > 2500 and self.salario <= 3500 and self.estado_civil == 'D'):
            return self.salario * 0.00
        elif (self.dependentes >= 5 and self.salario > 2500 and self.salario <= 3500 and self.estado_civil == 'D'):
            return self.salario * 0.00

    def desconto_salario_3500_4500_divorciado(self):
        if (self.dependentes <= 1 and self.salario > 3500 and self.salario <= 4500 and self.estado_civil == 'D'):
            return self.salario * 0.02
        elif (self.dependentes == 2 and self.salario > 3500 and self.salario <= 4500 and self.estado_civil == 'D'):
            return self.salario * 0.01
        elif (self.dependentes == 3 and self.salario > 3500 and self.salario <= 4500 and self.estado_civil == 'D'):
            return self.salario * 0.00
        elif (self.dependentes == 4 and self.salario > 3500 and self.salario <= 4500 and self.estado_civil == 'D'):
            return self.salario * 0.00
        elif (self.dependentes >= 5 and self.salario > 3500 and self.salario <= 4500 and self.estado_civil == 'D'):
            return self.salario * 0.00

    def desconto_salario_4500_divorciado(self):
        if (self.dependentes <= 1 and self.salario > 4500 and self.estado_civil == 'D'):
            return self.salario * 0.08
        elif (self.dependentes == 2 and self.salario > 4500 and self.estado_civil == 'D'):
            return self.salario * 0.07
        elif (self.dependentes == 3 and self.salario > 4500 and self.estado_civil == 'D'):
            return self.salario * 0.06
        elif (self.dependentes == 4 and self.salario > 4500 and self.estado_civil == 'D'):
            return self.salario * 0.04
        elif (self.dependentes >= 5 and self.salario > 4500 and self.estado_civil == 'D'):
            return self.salario * 0.01
    #######################################################################################################################

    def desconto_salario_1500_viuvo(self):
        if (self.dependentes <= 1 and self.salario <= 1500 and self.estado_civil == 'V'):
            return self.salario * 0.05
        elif (self.dependentes == 2 and self.salario <= 1500 and self.estado_civil == 'V'):
            return self.salario * 0.04
        elif (self.dependentes == 3 and self.salario <= 1500 and self.estado_civil == 'V'):
            return self.salario * 0.03
        elif (self.dependentes == 4 and self.salario <= 1500 and self.estado_civil == 'V'):
            return self.salario * 0.02
        elif (self.dependentes >= 5 and self.salario <= 1500 and self.estado_civil == 'V'):
            return self.salario * 0.01

    def desconto_salario_1500_2500_viuvo(self):
        if (self.dependentes <= 1 and self.salario > 1500 and self.salario <= 2500 and self.estado_civil == 'V'):
            return self.salario * 0.04
        elif (self.dependentes == 2 and self.salario > 1500 and self.salario <= 2500 and self.estado_civil == 'V'):
            return self.salario * 0.03
        elif (self.dependentes == 3 and self.salario > 1500 and self.salario <= 2500 and self.estado_civil == 'V'):
            return self.salario * 0.02
        elif (self.dependentes == 4 and self.salario > 1500 and self.salario <= 2500 and self.estado_civil == 'V'):
            return self.salario * 0.01
        elif (self.dependentes >= 5 and self.salario > 1500 and self.salario <= 2500 and self.estado_civil == 'V'):
            return self.salario * 0.00

    def desconto_salario_2500_3500_viuvo(self):
        if (self.dependentes <= 1 and self.salario > 2500 and self.salario <= 3500 and self.estado_civil == 'V'):
            return self.salario * 0.03
        elif (self.dependentes == 2 and self.salario > 2500 and self.salario <= 3500 and self.estado_civil == 'V'):
            return self.salario * 0.02
        elif (self.dependentes == 3 and self.salario > 2500 and self.salario <= 3500 and self.estado_civil == 'V'):
            return self.salario * 0.01
        elif (self.dependentes == 4 and self.salario > 2500 and self.salario <= 3500 and self.estado_civil == 'V'):
            return self.salario * 0.00
        elif (self.dependentes >= 5 and self.salario > 2500 and self.salario <= 3500 and self.estado_civil == 'V'):
            return self.salario * 0.00

    def desconto_salario_3500_4500_viuvo(self):
        if (self.dependentes <= 1 and self.salario > 3500 and self.salario <= 4500 and self.estado_civil == 'V'):
            return self.salario * 0.08
        elif (self.dependentes == 2 and self.salario > 3500 and self.salario <= 4500 and self.estado_civil == 'V'):
            return self.salario * 0.06
        elif (self.dependentes == 3 and self.salario > 3500 and self.salario <= 4500 and self.estado_civil == 'V'):
            return self.salario * 0.04
        elif (self.dependentes == 4 and self.salario > 3500 and self.salario <= 4500 and self.estado_civil == 'V'):
            return self.salario * 0.02
        elif (self.dependentes >= 5 and self.salario > 3500 and self.salario <= 4500 and self.estado_civil == 'V'):
            return self.salario * 0.00

    def desconto_salario_4500_viuvo(self):
        if (self.dependentes <= 1 and self.salario > 4500 and self.estado_civil == 'V'):
            return self.salario * 0.10
        elif (self.dependentes == 2 and self.salario > 4500 and self.estado_civil == 'V'):
            return self.salario * 0.08
        elif (self.dependentes == 3 and self.salario > 4500 and self.estado_civil == 'V'):
            return self.salario * 0.06
        elif (self.dependentes == 4 and self.salario > 4500 and self.estado_civil == 'V'):
            return self.salario * 0.04
        elif (self.dependentes >= 5 and self.salario > 4500 and self.estado_civil == 'V'):
            return self.salario * 0.02
    #######################################################################################################################

class Funcionario:
    def __init__(self, nome, nif, nis, estadocivil, dependentes, departamento, cargo, horastrabalhadas, valorhora, horaextra, valorhoraextra, baixamedica, iniciocontrato, morada,salario):
        self.nome = nome
        self.nif = nif
        self.nis = nis
        self.estadocivil = estadocivil
        self.dependentes = dependentes
        self.departamento = departamento
        self.cargo = cargo
        self.horastrabalhadas = horastrabalhadas
        self.valorhora = valorhora
        self.valorhoraextra = valorhoraextra
        self.horaextra = horaextra
        self.baixamedica = baixamedica
        self.iniciocontrato = iniciocontrato
        self.morada = morada
        self.salario = salario


    def nif(self):
        return self.nif

    def nis(self):
        return self.nis

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

    def imposto_ssc(self):
        return self.salario() * 0.11

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

    def morada(self):
        return self.morada

    def salarioliquido(self):
        return self.salario(self.valorhora * self.valorhoraextra) + (self.valorhoraextra * self.horaextra) - self.imposto_ssc() - (self.baixamedica * 30)

    def __str__(self):
        return f'Nome: {self.nome}\nNIF: {self.nif}\nNIS: {self.nis}\nEstado Civil: {self.estado_civil}\nDependentes: {self.dependentes}\nDepartamento: {self.departamento}\nCargo: {self.cargo}\nImposto: {self.imposto_ssc()}\nValor Hora Extra: {self.valorhoraextra}\nHoras Extra: {self.horaextra}\nBaixa Medica: {self.baixamedica}\nInício do Contrato: {self.iniciocontrato}\nMorada: {self.morada}\nSalario Bruto: {self.salario()}\nSalario Liquido: {self.salarioliquido()}\n'

print('Bem vindo ao sistema de cálculo de salario! \n')
nome = input('Digite o nome do funcionario: \n')
nif = int(input('Digite o NIF do funcionario: \n'))
nis = int(input('Digite o NIS do funcionario: \n'))
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
print('----------------------------------------')
funcionario = Funcionario(nome, nif, nis, estadocivil, dependentes, departamento, cargo, horastrabalhadas, valorhora, horaextra, valorhoraextra, baixamedica, iniciocontrato, morada)

print(funcionario)

