'''
1 - Considere uma entidade Funcionário, que possui nome, data de admissão e salário.
Implemente sua classe, definindo também alguns mérodos para manipulação de atributos.
Em seguida, considere a entidade Gerente, que também é funcionário. 
Além dos atributos de funcionário, ele também recebe um bônus que é a porcentagem adfuicuibal aplicada ao salário.
Implemente a classe Gerente como uma extensão de Funcionário.


Passo 1 - Organização dos requisitos
Atributos:
Nome
Data de Admssão
Setor
Cargo
Salario

Métodos
AlterarSalario
ComissaoBonus

'''

class Funcionario:
    def __init__(self, nome, data_admissao, setor, cargo, salario):
        self.nome = nome
        self.data_admissao = data_admissao
        self.setor = setor
        self.cargo = cargo
        self.salario = salario

    def altera_salario (self, novo_salario):
        self.salario = novo_salario

    def comissao_bonus (self, percentual):
        self.salario += self.salario + (percentual / 100)

    def mostrar_informacoes(self):
        return f"Nome: {self.nome}, Admissão: {self.data_admissao}, Salário: R${self.salario:2f}"
    

class Gerente(Funcionario):
    def __init__(self, nome, data_admissao, setor, cargo, salario, bonus):
        super().__init__(nome, data_admissao, setor, cargo, salario) # herda atributos
        self.bonus = bonus                                              # novo atributo

    def calcular_salario_com_bonus(self):
        return self.salario + (self.salario * (self.bonus / 100))
    
    def mostrar_informacoes(self):
        base = super().mostrar_informacoes()
        return base +f", Bônus: {self.bonus}%"
    


a1 = Funcionario("Maria", "07/12/2017", "Governança", "Analista", 1600)
a2 = Gerente("João", "15/03/2016", "Governança", "Gerente", 2500, 30,)


print(a1.mostrar_informacoes())
print(a2.mostrar_informacoes(), a2.calcular_salario_com_bonus())