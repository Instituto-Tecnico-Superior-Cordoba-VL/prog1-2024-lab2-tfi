from datos_almacen import Producto, Proveedor, Venta, Almacen

proveedor_1 = Proveedor("Juan",4804828,"Av. Siempreviva 234")

print(proveedor_1.nombre)

producto_1 = Producto("Arroz", "Mandisovi", 300.00, 600.00, "Juan")

print (producto_1.nombre)
print (producto_1.marca)
print (producto_1.stock)

producto_1.comprar(50)
producto_1.comprar(20)
print (producto_1.stock)

venta_1 = Venta(1,2023,11,2,"Arroz",2,600.00)
producto_1.vender(2)

print(venta_1.producto_vendido)
print(venta_1.monto)

print (producto_1.nombre)
print (producto_1.marca)
print (producto_1.stock)

almacen = Almacen()

almacen.agregar_proveedor(proveedor_1)
