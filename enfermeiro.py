from funcionario import Funcionario

class Enfermeiro(Funcionario):
    def __init__(self, nome, id_funcionario, setor):
        super().__init__(nome, id_funcionario)
        self.setor = setor
