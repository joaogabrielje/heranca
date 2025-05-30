from funcionario import Funcionario

class Dentista(Funcionario):
    def __init__(self, nome, id_funcionario, especialidade):
        super().__init__(nome, id_funcionario)
        self.especialidade = especialidade
