from agenda import Agenda,Contacto
# Test crear agenda
agenda = Agenda()
assert agenda.contar_contactos() == 0 # True

# test agregar contacto
agenda.agregar_contacto("Matias",4804828)
assert agenda.contar_contactos() == 1

# test guardar y cargar agenda en archivo
agenda.guardar_contactos()
agenda2 = Agenda()
agenda2.cargar_contactos()

assert agenda2.contar_contactos() == 1

agenda2.imprimir_contactos_numeros()
