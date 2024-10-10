import pickle #libreria para guardar y recuperar informacion

class Socio():
    def __init__(self,dni,nombre,telefono,domicilio):
        """ Crea un socio nuevo con los datos indicados """
        self.dni =dni
        self.nombre = nombre
        self.telefono = telefono
        self.domicilio = domicilio

    def __str__(self):
        """ Devuelve una cadena con la informacion del socio """
        return "DNI: {self.dni}\nNombre: {self.nombre}\nTelefono: {self.telefono}\nDomicilio: {self.domicilio}\n"

class Pelicula():
    def __init__(self,titulo,genero,anio):
        """ Crea una pelicula nueva con los datos indicados """
        self.titulo = titulo
        self.genero = genero
        self.anio = anio
        self.alquilada = None
    
    def __str__(self):
        """ Devuelve una cadena con la informacion de la pelicula """
        return f"Titulo: {self.titulo}\nGenero: {self.genero}\nAño: {self.anio}\nAlquilada: {self.alquilada}"

    def esta_alquilada(self):
        return self.alquilada != None

class Videoclub:
    def __init__(self):
        """ Crea la lista de socios y peliculas """
        self.socios = []
        self.peliculas = []

    def contiene_socio(self,dni)->bool:
        """ Indica si un socio existe o no en la base"""
        esta = False
        for socio in self.socios:
            if socio.dni == dni:
                esta = True
        return esta

    def buscar_socio(self,dni)->"Socio":
        """ Si esta devuelve el socio con el dni buscado, sino devuelve None"""
        devolver = None
        for socio in self.socios:
            if socio.dni == dni:
                devolver = socio
        return devolver

    def alta_nuevo_socio(self,socio)->None:
        """ Agrega un nuevo socio a la base """
        self.socios.append(socio)
        
    def baja_socio(self,dni)-> None:
        """Borra un socio de la base"""
        socio = self.buscar_socio(dni)
        self.socios.remove(socio)
    
    def mostrar_socios(self)->None:
        """ Imprime en pantalla los datos de todos los socios"""
        for socio in self.socios:
            print (socio)
    
    def contiene_pelicula(self,titulo)->bool:
        """ Indica si una película existe o no en la base"""
        esta = False
        for pelicula in self.peliculas:
            if pelicula.titulo == titulo:
                esta = True
        return esta
    def buscar_pelicula(self,titulo)->"Pelicula":
        """ Si está devuelve la película con el título buscado, sino devuelve None"""
        esta = False
        for pelicula in self.peliculas:
            if pelicula.titulo == titulo:
                devolver = pelicula
        return devolver
        
    def alta_nueva_pelicula(self,pelicula)->None:
        self.peliculas.append(pelicula)
        
    def baja_pelicula(self,titulo)->None:
        pelicula = self.buscar_pelicula(titulo)
        self.peliculas.remove(pelicula)
        
    def alquilar_pelicula(self,titulo,dni)-> None:
        for pelicula in self.peliculas:
            if pelicula.titulo == titulo and pelicula.alquilada == None:
                pelicula.alquilada = dni
                
    def devolver_pelicula(self,titulo)->None:
        for pelicula in self.peliculas:
            if pelicula.titulo == titulo and pelicula.alquilada != None:
                pelicula.alquilada = None
    
    def mostrar_pelicula_genero(self,genero)->None:
        for pelicula in self.peliculas:
            if pelicula.genero.lower() == pelicula.genero.lower():
                print (pelicula)
         
    def guardar_archivo(self,archivo="video.pickle"):
        pickle_file = open(archivo, 'wb')
        pickle.dump(self, pickle_file)
        pickle_file.close()

    def leer_archivo(self,archivo="video.pickle"):
        pickle_file = open(archivo,'rb')
        video = pickle.load(pickle_file)
        self.socios = video.socios
        self.peliculas = video.peliculas
        pickle_file.close()

