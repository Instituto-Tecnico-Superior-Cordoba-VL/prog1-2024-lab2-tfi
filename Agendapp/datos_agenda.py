import pickle

#modelo
class Contacto:
    def __init__(self, nombre, numero):
        self.nombre = nombre
        self.numero = numero

class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, nombre, numero):
        contacto = Contacto(nombre, numero)
        self.contactos.append(contacto)

    def buscar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                return contacto.numero
        return -1

    def modificar_contacto(self, nombre, nuevo_numero):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                contacto.numero = nuevo_numero

    def eliminar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                self.contactos.remove(contacto)
                return 1
        return -1
    
    def contar_contactos(self):
        return len(self.contactos)

    def imprimir_contactos(self):
        for contacto in self.contactos:
            print(contacto.nombre)

    def imprimir_numeros(self):
        for contacto in self.contactos:
            print(contacto.numero)

    def imprimir_contactos_numeros(self):
        for contacto in self.contactos:
            print(f"{contacto.nombre}: {contacto.numero}")

    def guardar_contactos(self, archivo="agenda.pickle"):
        archivo_pickle = open(archivo, 'wb')
        pickle.dump(self.contactos, archivo_pickle)
        archivo_pickle.close()

    def cargar_contactos(self, archivo="agenda.pickle"):
        archivo_pickle = open(archivo, 'rb')
        self.contactos = pickle.load(archivo_pickle)
        archivo_pickle.close()