from datos_almacen import Producto, Venta, Proveedor, Almacen

def menu()->int:
    """ Funcion que no toma nada y devuelve una opcion del menu ingresada por el usuari"""
    opcion = 0
    while opcion < 1 or opcion > 9:
        print("--")
        print("(1) Dar de alta nuevo producto")
        print("(2) Dar de baja producto")
        print("(3) Dar de alta nuevo proveedor")
        print("(4) Dar de baja proveedor")
        print("(5) Hacer venta")
        print("(6) Mostrar base de datos")
        print("(7) Guardar archivo")
        print("(8) Leer archivo")
        print("(9) Salir")
        print("--")
        opcion = int(input("Elija una opcion: "))
        print("--")
    return opcion

def run(almacen)->None:
    """Funcion que usa el menu e interactua con el usuario para manipular un dato tipo almacen
    Entrada: almacen es de la clase Almacen
    Salida: Nada
    """
    opcion = 0
    while opcion != 9: # 9 es el numero que uso para salir del programa
        opcion = menu()
        if opcion == 1:
            """
        self.nombre = nombre
        self.marca = marca
        self.precio_compra = precio_compra
        self.precio_venta = precio_venta
        self.nombre_proveedor = nombre_proveedor
        """
            nombre = input("Nombre: ")
            marca = input("marca: ")
            precio_compra = input("precio_compra: ")
            precio_venta = input("precio_venta: ")
            nombre_proveedor = input("nombre_proveedor: ")
            producto = Producto(nombre,marca,precio_compra,precio_venta,nombre_proveedor)
            if almacen.contiene_producto(producto.nombre):
                print("El producto ya existe")
            else:
                if almacen.contiene_proveedor(producto.proveedor):
                    almacen.alta_producto(producto)
                    print("Producto Agregado")
                else:
                    print("El proveedor del producto no esta en la BD")
        if opcion == 2:
            dni = input("Dni:")
            if videoclub.contiene_socio(dni):
                print("El socio no existe")
            else:
                videoclub.baja_socio(socio)
                print("Socio dado de baja")
        if opcion == 3:
            titulo = input("Titulo: ")
            genero = input("Genero: ")
            anio = input("Anio: ")
            peli = Pelicula(titulo,genero,anio)
            if videoclub.contiene_pelicula(peli.titulo):
                print("La peli ya existe")
            else:
                videoclub.alta_nueva_pelicula(peli)
                print("Pelicula agregada")
        if opcion == 4:
            dni = input("Titulo:")
            if videoclub.contiene_pelicula(dni):
                print("La pelicula no existe")
            else:
                videoclub.baja_pelicula(socio)
                print("Pelicula ha sido dada de baja")
        if opcion == 5:
            titulo = input("Titulo: ")
            dni = input("DNI socio: ")
            if videoclub.contiene_pelicula() and videoclub.contiene_socio():
                videoclub.alquilar_pelicula(titulo,dni)
            else:
                print("No se pudo alquilar la pelicula")
        if opcion == 6:
            titulo = input("Titulo: ")
            if not videoclub.contiene_pelicula(titulo):
                print("La pelicula no existe")
            else:
                videoclub.devolver_pelicula(titulo)
                print("Pelicula ha sido devuelta")
        if opcion == 7:
            videoclub.guardar_archivo()
        if opcion == 8:
            videoclub.leer_archivo()
        print("Productos: ", len(almacen.productos))
        print("Proveedores: ", len(almacen.proveedores))
        print("Ventas: ", len(almacen.ventas))


if __name__ == "__main__":
    almacen = Almacen()
    run(almacen)
