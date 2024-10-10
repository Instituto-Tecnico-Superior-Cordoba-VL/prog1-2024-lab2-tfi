class Producto:
    def __init__(self,nombre:str,marca:str,precio_compra:float,precio_venta:float, nombre_proveedor:str):
        self.nombre = nombre
        self.marca = marca
        self.stock = 0
        self.precio_compra = precio_compra
        self.precio_venta = precio_venta
        self.nombre_proveedor = nombre_proveedor
    
    def comprar(self,cantidad):
        self.stock = self.stock + cantidad
    def vender(self,cantidad):
        self.stock = self.stock - cantidad

class Proveedor:
    def __init__(self,nombre:str,tel:int,direccion:str):
        self.nombre = nombre
        self.telefono = tel
        self.direccion = direccion

class Venta:
    def __init__(self,n_factura,anio,mes,dia,p_vendido, cantidad, precio_unitario):
        self.n_factura = n_factura
        self.anio = anio
        self.mes = mes
        self.dia = dia
        self.producto_vendido = p_vendido
        self.cantidad = cantidad
        self.monto = cantidad * precio_unitario

class Almacen:
    def __init__(self):
        self.productos = []
        self.proveedores = []
        self.ventas = []
    
    def alta_producto(self,producto)->None:
        """Agrega un producto a la lista de productos"""
        self.productos.append(producto)
    
    def contiene_producto(self,nombre_producto)->bool:
        """dice si un producto est´a o no est´a en la lista"""
        esta = False
        for producto_i in self.productos:
            if producto_i.nombre == nombre_producto:
                esta = True
        return esta
        
    def agregar_proveedor(self,proveedor):
        self.proveedores.append(proveedor)