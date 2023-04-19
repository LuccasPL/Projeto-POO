# calculo de salario, imposto e desconto, com base em horas trabalhadas e valor da hora, com base em uma classe
# usar o padx = para distanciar os elementos na horizontal / pady = para distanciar os elementos na vertical 

class Funcionario:
    def __init__(self, nome, estadocivil, dependentes, departamento, cargo, horastrabalhadas, valorhora, horaextra, valorhoraextra, baixamedica, iniciocontrato, morada):
        self.nome = nome
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

    def estado_civil(self):
        return self.estadocivil

    def dependentes(self):
        return self.dependentes

    def departamento(self):
        return self.departamento

    def imposto_ssc(self):
        return self.salario() * 0.11

    def desconto(self):
        return self.salario() * 0.08

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
        return self.salario() + (self.valorhoraextra * self.horaextra) - self.imposto_ssc() - self.desconto() - (self.baixamedica * 30)

    def __str__(self):
        return f'Nome: {self.nome}\nEstado Civil: {self.estado_civil}\nDependentes: {self.dependentes}\nDepartamento: {self.departamento}\nCargo: {self.cargo}\nSalario Bruto: {self.salario()}\nImposto: {self.imposto_ssc()}\nDesconto: {self.desconto()}\nDias Trabalhados: {self.diastrabalhados}\nValor Hora Extra: {self.valorhoraextra}\nHoras Extra: {self.horaextra}\nBaixa Medica: {self.baixamedica}\nInício do Contrato: {self.iniciocontrato}\nMorada: {self.morada}\nSalario Liquido: {self.salarioliquido()}\n'

print('Bem vindo ao sistema de calculo de salario! \n')
nome = input('Digite o nome do funcionario: \n')
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
funcionario = Funcionario(nome, estadocivil, dependentes, cargo, horastrabalhadas, valorhora, horaextra, valorhoraextra, baixamedica, iniciocontrato, morada,)

print(funcionario)

