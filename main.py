from dentista import Dentista
from enfermeiro import Enfermeiro
from cliente import Cliente
from agendamento import Agendamento

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
print(f"Agendamentos do dentista {dentista1.nome}:")
for ag in dentista1.agendamentos:
    print(f"- {ag.cliente.nome} em {ag.data} às {ag.horario}")

print(f"\nAgendamentos do enfermeiro {enfermeiro1.nome}:")
for ag in enfermeiro1.agendamentos:
    print(f"- {ag.cliente.nome} em {ag.data} às {ag.horario}")
