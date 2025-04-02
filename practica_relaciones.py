#practica de David Fernando Mita Tejada
class Producto:
    def __init__(self, nombre_producto, precio, stock):
        self.nombre_producto = nombre_producto
        self.precio = precio
        self.stock = stock
    def __str__(self):
        return f"{self.nombre_producto} - Precio: {self.precio}, Stock: {self.stock}"
    
    def __repr__(self):
        return self.__str__()
    
    def reducir_stock(self, cantidad):
        if self.stock >= cantidad:
            self.stock -= cantidad
            return True
        return False
    
    def reponer_stock(self, cantidad):
        self.stock += cantidad

class MaquinaExpendedora:
    def __init__(self):
        self.productos = {}
        self.saldo = 0

    def agregar_producto(self, producto):
        self.productos[producto.nombre_producto] = producto

    def mostrar_productos(self):
        for clave, valor in self.productos.items():
            print(f"{clave}: {valor}")
        return self.productos 
    
    def seleccionar_producto(self, nombre_producto):
        if nombre_producto in self.productos and self.productos[nombre_producto].stock > 0:
            return self.productos[nombre_producto]
        return None
    
    def insertar_monedas(self, monto):
        self.saldo += monto
    
    def procesar_compra(self, nombre_producto):
        producto = self.seleccionar_producto(nombre_producto)
        if not producto:
            return "Producto no disponible"
        
        if self.saldo < producto.precio:
            return "Saldo insuficiente"
        
        if producto.reducir_stock(1):
            self.saldo -= producto.precio
            ticket = f"Compra exitosa: {producto.nombre_producto}, Cambio: {self.saldo}"
            self.saldo = 0  # Se devuelve el cambio restante
            return print(ticket)
        else:
            return "Stock insuficiente"

class Encargado:
    def __init__(self, nombre_producto):
        self.nombre_producto = nombre_producto
    
    def reponer_producto(self, maquina, nombre_producto, cantidad):
        if nombre_producto in maquina.productos:
            maquina.productos[nombre_producto].reponer_stock(cantidad)
            return f"Se han repuesto {cantidad} unidades de {nombre_producto}"
        return "Producto no encontrado"

maquina = MaquinaExpendedora()

maquina.agregar_producto(Producto("Coca-Cola", 10, 5))
maquina.agregar_producto(Producto("Jugo de Naranja", 12, 3))

maquina.mostrar_productos()
maquina.insertar_monedas(15)
maquina.procesar_compra("Coca-Cola")
print(maquina.mostrar_productos())

encargado = Encargado("Juan")
print(encargado.reponer_producto(maquina, "Coca-Cola", 10))
print(maquina.mostrar_productos())