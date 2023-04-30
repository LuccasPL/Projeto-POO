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
    #######################################################################################################################

class Funcionario:
    def __init__(self, nome, nif, niss, estadocivil, dependentes, departamento, cargo, horastrabalhadas, valorhora, horaextra, valorhoraextra, baixamedica, iniciocontrato, morada):
        self.nome = nome
        self.nif = nif
        self.niss = niss
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

    def salario(self):
        return self.horastrabalhadas * self.valorhora

    def nif(self):
        return self.nif

    def niss(self):
        return self.niss

    def estado_civil(self):
        if self.estadocivil == 'S':
            return 'Solteiro'
        elif self.estadocivil == 'C':
            return 'Casado'
        elif self.estadocivil == 'V':
            return 'Viúvo'
        elif self.estadocivil == 'D':
            return 'Divorciado'


    def dependentes(self):
        return self.dependentes

    def departamento(self):
        return self.departamento

    def imposto_ssc(self):
        return self.salario() * 0.11
# criar funcao de acordo com o estado civil, dependentes e salario
    def desconto_solteiro_0_dependente(self):
        if self.dependentes == 0 and self.salario() <= 900 and self.estadocivil == 'S':
            return 0
        elif self.dependentes == 1:
            return self.salario() * 0.08
        elif self.dependentes == 2:
            return self.salario() * 0.06
        elif self.dependentes == 3:
            return self.salario() * 0.04
        elif self.dependentes == 4:
            return self.salario() * 0.02
        elif self.dependentes >= 5:
            return self.salario() * 0.00

    def desconto_casado_0_dependente(self):
        if self.dependentes == 0 and self.salario() <= 900 and self.estadocivil == 'C':
            return 0
        elif self.dependentes == 1:
            return self.salario() * 0.12
        elif self.dependentes == 2:
            return self.salario() * 0.10
        elif self.dependentes == 3:
            return self.salario() * 0.08
        elif self.dependentes == 4:
            return self.salario() * 0.06
        elif self.dependentes >= 5:
            return self.salario() * 0.04

    def desconto_viuvo_0_dependente(self):
        if self.dependentes == 0 and self.salario() <= 900 and self.estadocivil == 'V':
            return 0
        elif self.dependentes == 1:
            return self.salario() * 0.10
        elif self.dependentes == 2:
            return self.salario() * 0.08
        elif self.dependentes == 3:
            return self.salario() * 0.06
        elif self.dependentes == 4:
            return self.salario() * 0.04
        elif self.dependentes >= 5:
            return self.salario() * 0.02

    def desconto_divorciado_0_dependente(self):
        if self.dependentes == 0 and self.salario() <= 900 and self.estadocivil == 'D':
            return 0
        elif self.dependentes == 1:
            return self.salario() * 0.10
        elif self.dependentes == 2:
            return self.salario() * 0.08
        elif self.dependentes == 3:
            return self.salario() * 0.06
        elif self.dependentes == 4:
            return self.salario() * 0.04
        elif self.dependentes >= 5:
            return self.salario() * 0.02

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
        return self.salario() + (self.valorhoraextra * self.horaextra) - self.imposto_ssc() - (self.baixamedica * 30)

    def __str__(self):
        return f'Nome: {self.nome}\nNIF: {self.nif}\nNISS: {self.niss}\nEstado Civil: {self.estado_civil}\nDependentes: {self.dependentes}\nDepartamento: {self.departamento}\nCargo: {self.cargo}\nImposto: {self.imposto_ssc()}\nValor Hora Extra: {self.valorhoraextra}\nHoras Extra: {self.horaextra}\nBaixa Medica: {self.baixamedica}\nInício do Contrato: {self.iniciocontrato}\nMorada: {self.morada}\nSalario Bruto: {self.salario()}\nSalario Liquido: {self.salarioliquido()}\n'

print('Bem vindo ao sistema de cálculo de salario! \n')
nome = input('Digite o nome do funcionario: \n')
nif = int(input('Digite o NIF do funcionario: \n'))
niss = int(input('Digite o NISS do funcionario: \n'))
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
funcionario = Funcionario(nome, nif, niss, estadocivil, dependentes, departamento, cargo, horastrabalhadas, valorhora, horaextra, valorhoraextra, baixamedica, iniciocontrato, morada)

print(funcionario)

