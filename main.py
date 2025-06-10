from dentista import Dentista
from enfermeiro import Enfermeiro
from cliente import Cliente
from agendamento import Agendamento

funcionarios = []
clientes = []
agendamentos = []

# Criar profissionais
dentista1 = Dentista("Dra. Ana", 101, "Ortodontia")
enfermeiro1 = Enfermeiro("Carlos", 202, "Pediatria")

# Criar clientes
cliente1 = Cliente("Lucas", "lucas@email.com")
cliente2 = Cliente("Mariana", "mariana@email.com")

# Criar agendamentos
ag1 = Agendamento(cliente1, dentista1, "06-01-2025", "09:00")
ag2 = Agendamento(cliente2, enfermeiro1, "06-01-2025", "10:30")

# Associar os agendamentos ao funcionário correspondente
dentista1.agendamentos.append(ag1)
enfermeiro1.agendamentos.append(ag2)

# Exibir agendamentos dos funcionários

def menu ():
  
  print('-----------------------------------')
  print('------SISTEMA DE AGENDAMENTOS------')
  print('-----------------------------------\n')
  print('1- Cadastrar funcionario')
  print('2- Cadastrar cliente')
  print('3- Fazer agendamento')
  print('4- Sair\n')


def fun_cad ():
  
  print('------CADASTRO DE FUNCIONARIO------\n')
  print('Qual o tipo:')
  print('1- Dentista')
  print('2- Enfermeiro\n')
  tipo_fun = input('Escolha uma das opções: ')
  
  nome = input('Digite o nome do funcinario:')

  id_fun = input('Qual o id do funcionario:')

  if tipo_fun == '1':
    esp = input('Qual a especialidade do(a) dentista: ')
    funcionario = Dentista(nome, id_fun, esp)
  
  elif tipo_fun == '2':
    setor = input('Qual o setor do(a) enfermeiro(a): ')
    funcionario = Enfermeiro(nome, id_fun, setor)

  else:
    print('Tipo invalido')
    return
  
  funcionarios.append(funcionario)
  print('Funcionario cadastrado com sucesso\n')


while True:
  menu()
  opcao = input('Escolha uma opção: \n')

  if opcao == '4':
    print('Obrigado por usar nosso sitema...')
    break
  
  elif opcao == '1':
    fun_cad()

  else:
    print('Opção invalida, tente novamente')
  
