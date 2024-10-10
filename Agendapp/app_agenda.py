from agenda import Agenda,Contacto

def menu()->int: # interfaz grafica
    opcion = 0
    while opcion < 1 or opcion > 7:
        print("--")
        print("(1) Agregar contacto")
        print("(2) Buscar contacto")
        print("(3) Eliminar contacto")
        print("(4) Imprimir agenda")
        print("(5) Guardar en archivo")
        print("(6) Cargar desde archivo")
        print("(7) Salir")
        print("--")
        opcion = int(input("Elija una opción: "))
        print("--")
    return opcion

def ejecutar(agenda): # controlador
    opcion = 0
    while opcion != 7:
        opcion = menu()
        if opcion == 1: # Agregar contacto
            nombre = input("Nombre: ")
            numero = input("Número de teléfono: ")
            agenda.agregar_contacto(nombre, numero)
            print("Contacto agregado")
        if opcion == 2:
            nombre = input("Nombre: ")
            respuesta = agenda.buscar_contacto(nombre)
            if respuesta != -1:
                print(f"El número de teléfono de {nombre} es: {respuesta}")
            else:
                print(f"{nombre} no se encuentra en la agenda.")
        if opcion == 3:
            nombre = input("Nombre: ")
            respuesta = agenda.eliminar_contacto(nombre)
            if respuesta != -1:
                print(f"{nombre} ha sido eliminado de la agenda.")
            else:
                print(f"{nombre} no se encuentra en la agenda.")
        if opcion == 4:
            agenda.imprimir_contactos_numeros()
        if opcion == 5:
            agenda.guardar_contactos()
        if opcion == 6:
            agenda.cargar_contactos()

if __name__ == "__main__":
    agenda = Agenda()
    ejecutar(agenda)
